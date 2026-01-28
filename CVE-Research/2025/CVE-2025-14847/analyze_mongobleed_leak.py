#!/usr/bin/env python3
"""
MongoBleed Leaked Data Analyzer
Parses and categorizes leaked memory from CVE-2025-14847 exploit
"""

import re
import sys
import json
from collections import defaultdict

class LeakedDataAnalyzer:
    def __init__(self, filepath):
        self.filepath = filepath
        self.raw_data = ""
        self.results = defaultdict(list)
        
    def load_data(self):
        """Load leaked binary data"""
        try:
            with open(self.filepath, 'rb') as f:
                self.raw_data = f.read().decode('utf-8', errors='ignore')
            print(f"✅ Loaded {len(self.raw_data)} bytes from {self.filepath}\n")
        except Exception as e:
            print(f"❌ Error loading file: {e}")
            sys.exit(1)
    
    def extract_strings(self, min_length=4):
        """Extract printable strings from binary data"""
        pattern = re.compile(rb'[\x20-\x7e]{' + str(min_length).encode() + rb',}')
        with open(self.filepath, 'rb') as f:
            data = f.read()
        strings = [s.decode('utf-8', errors='ignore') for s in pattern.findall(data)]
        return strings
    
    def analyze_docker_info(self):
        """Extract Docker/Container related information"""
        # Container IDs (64 char hex)
        container_ids = re.findall(r'\b[0-9a-f]{64}\b', self.raw_data)
        if container_ids:
            self.results['container_ids'] = list(set(container_ids))
        
        # Docker volumes
        volumes = re.findall(r'/var/lib/docker/volumes/[^\s]+', self.raw_data)
        if volumes:
            self.results['volumes'] = list(set(volumes))
        
        # Overlay2 layers
        overlays = re.findall(r'/var/lib/docker/overlay2/[^\s:]+', self.raw_data)
        if overlays:
            self.results['overlay_layers'] = list(set(overlays))
        
        # Container paths
        container_paths = re.findall(r'/var/lib/docker/containers/[^\s]+', self.raw_data)
        if container_paths:
            self.results['container_paths'] = list(set(container_paths))
    
    def analyze_mongodb_logs(self):
        """Extract MongoDB log entries"""
        # JSON log format
        json_pattern = r'\{[^}]*"s":\s*"[DI]"[^}]*"c":\s*"[A-Z]+"[^}]*\}'
        logs = re.findall(json_pattern, self.raw_data)
        
        parsed_logs = []
        for log in logs:
            try:
                log_data = json.loads(log)
                parsed_logs.append({
                    'severity': log_data.get('s', 'U'),
                    'component': log_data.get('c', 'Unknown'),
                    'id': log_data.get('id', 'N/A'),
                    'context': log_data.get('ctx', 'N/A'),
                    'message': log_data.get('msg', 'N/A')
                })
            except:
                pass
        
        if parsed_logs:
            self.results['mongodb_logs'] = parsed_logs
    
    def analyze_errors(self):
        """Extract error messages"""
        # BSON errors
        bson_errors = re.findall(r'InvalidBSON:[^"\n]+', self.raw_data)
        if bson_errors:
            self.results['bson_errors'] = list(set(bson_errors))
        
        # Error messages
        error_msgs = re.findall(r'"errMsg":\s*"([^"]+)"', self.raw_data)
        if error_msgs:
            self.results['error_messages'] = list(set(error_msgs))
    
    def analyze_network_info(self):
        """Extract network related information"""
        # Connection info
        connections = re.findall(r'conn\d+', self.raw_data)
        if connections:
            self.results['connections'] = list(set(connections))[:20]  # Limit to 20
        
        # IP addresses
        ips = re.findall(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}(?::\d+)?\b', self.raw_data)
        if ips:
            self.results['ip_addresses'] = list(set(ips))
        
        # UUIDs
        uuids = re.findall(r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}', self.raw_data)
        if uuids:
            self.results['uuids'] = list(set(uuids))
    
    def analyze_filesystem(self):
        """Extract filesystem paths"""
        # Host paths
        host_paths = re.findall(r'/home/[^\s:]+', self.raw_data)
        if host_paths:
            self.results['host_paths'] = list(set(host_paths))
        
        # System paths
        sys_paths = re.findall(r'/(?:proc|sys|dev)/[^\s]+', self.raw_data)
        if sys_paths:
            self.results['system_paths'] = list(set(sys_paths))[:30]  # Limit output
        
        # Device files
        devices = re.findall(r'/dev/[a-z]+\d*', self.raw_data)
        if devices:
            self.results['devices'] = list(set(devices))
    
    def analyze_system_stats(self):
        """Extract system statistics"""
        # Load averages
        load_avgs = re.findall(r'avg\d+=[\d.]+', self.raw_data)
        if load_avgs:
            self.results['load_averages'] = list(set(load_avgs))
        
        # Memory stats
        mem_stats = re.findall(r'(?:mem|memory)[:\s]+\d+', self.raw_data, re.IGNORECASE)
        if mem_stats:
            self.results['memory_stats'] = list(set(mem_stats))[:10]
    
    def analyze_mount_info(self):
        """Extract filesystem mount information"""
        mount_lines = re.findall(r'\d+ \d+ \d+:\d+ / [^\n]+', self.raw_data)
        if mount_lines:
            parsed_mounts = []
            for line in mount_lines[:15]:  # Limit to 15 mounts
                parts = line.split()
                if len(parts) >= 5:
                    parsed_mounts.append({
                        'mount_id': parts[0],
                        'parent_id': parts[1],
                        'device': parts[2],
                        'mount_point': parts[4] if len(parts) > 4 else 'unknown'
                    })
            self.results['mounts'] = parsed_mounts
    
    def analyze_all(self):
        """Run all analysis functions"""
        print("🔍 Analyzing leaked data...\n")
        self.analyze_docker_info()
        self.analyze_mongodb_logs()
        self.analyze_errors()
        self.analyze_network_info()
        self.analyze_filesystem()
        self.analyze_system_stats()
        self.analyze_mount_info()
    
    def print_results(self):
        """Print formatted results"""
        print("=" * 80)
        print("🚨 MONGOBLEED (CVE-2025-14847) LEAKED DATA ANALYSIS")
        print("=" * 80)
        print()
        
        # Docker/Container Information
        if self.results['container_ids']:
            print("📦 CONTAINER IDs (Critical)")
            print("-" * 80)
            for cid in self.results['container_ids']:
                print(f"  • {cid}")
            print()
        
        if self.results['volumes']:
            print("💾 DOCKER VOLUMES")
            print("-" * 80)
            for vol in self.results['volumes'][:10]:
                print(f"  • {vol}")
            if len(self.results['volumes']) > 10:
                print(f"  ... and {len(self.results['volumes']) - 10} more")
            print()
        
        if self.results['overlay_layers']:
            print("🗂️  OVERLAY2 LAYERS")
            print("-" * 80)
            print(f"  Total layers found: {len(self.results['overlay_layers'])}")
            for layer in self.results['overlay_layers'][:5]:
                print(f"  • {layer}")
            if len(self.results['overlay_layers']) > 5:
                print(f"  ... and {len(self.results['overlay_layers']) - 5} more")
            print()
        
        if self.results['container_paths']:
            print("📁 CONTAINER PATHS")
            print("-" * 80)
            for path in self.results['container_paths'][:5]:
                print(f"  • {path}")
            print()
        
        # Filesystem Information
        if self.results['host_paths']:
            print("🏠 HOST SYSTEM PATHS")
            print("-" * 80)
            for path in self.results['host_paths']:
                print(f"  • {path}")
            print()
        
        if self.results['devices']:
            print("💿 DEVICE FILES")
            print("-" * 80)
            for dev in self.results['devices']:
                print(f"  • {dev}")
            print()
        
        # Network Information
        if self.results['ip_addresses']:
            print("🌐 IP ADDRESSES")
            print("-" * 80)
            for ip in self.results['ip_addresses']:
                print(f"  • {ip}")
            print()
        
        if self.results['uuids']:
            print("🔑 UUIDs")
            print("-" * 80)
            for uuid in self.results['uuids']:
                print(f"  • {uuid}")
            print()
        
        if self.results['connections']:
            print("🔌 CONNECTION IDs (Sample)")
            print("-" * 80)
            print(f"  Total connections: {len(self.results['connections'])}")
            for conn in self.results['connections'][:10]:
                print(f"  • {conn}")
            print()
        
        # MongoDB Logs
        if self.results['mongodb_logs']:
            print("📝 MONGODB LOG ENTRIES")
            print("-" * 80)
            print(f"  Total log entries: {len(self.results['mongodb_logs'])}")
            for i, log in enumerate(self.results['mongodb_logs'][:5], 1):
                print(f"  [{i}] {log['severity']}/{log['component']} (id:{log['id']}) - {log['context']}")
                print(f"      Message: {log['message'][:70]}...")
            print()
        
        # Errors
        if self.results['bson_errors']:
            print("⚠️  BSON ERRORS")
            print("-" * 80)
            for err in self.results['bson_errors'][:5]:
                print(f"  • {err}")
            print()
        
        if self.results['error_messages']:
            print("❌ ERROR MESSAGES")
            print("-" * 80)
            for msg in self.results['error_messages'][:5]:
                print(f"  • {msg[:100]}...")
            print()
        
        # System Information
        if self.results['mounts']:
            print("🔧 FILESYSTEM MOUNTS (Sample)")
            print("-" * 80)
            for mount in self.results['mounts'][:10]:
                print(f"  • Mount ID {mount['mount_id']}: {mount['mount_point']} ({mount['device']})")
            print()
        
        if self.results['load_averages']:
            print("📊 SYSTEM LOAD METRICS")
            print("-" * 80)
            for stat in self.results['load_averages'][:10]:
                print(f"  • {stat}")
            print()
        
        # Summary
        print("=" * 80)
        print("📈 SUMMARY")
        print("=" * 80)
        total_items = sum(len(v) if isinstance(v, list) else 1 for v in self.results.values())
        print(f"  Total unique data points extracted: {total_items}")
        print(f"  Categories found: {len(self.results)}")
        print()
        
        # Risk Assessment
        print("🚨 RISK ASSESSMENT")
        print("=" * 80)
        risk_score = 0
        if self.results['container_ids']:
            print("  [CRITICAL] Container IDs exposed - Container escape possible")
            risk_score += 10
        if self.results['volumes']:
            print("  [CRITICAL] Volume paths exposed - Direct data access possible")
            risk_score += 10
        if self.results['overlay_layers']:
            print("  [HIGH] Overlay layers exposed - Filesystem structure revealed")
            risk_score += 5
        if self.results['host_paths']:
            print("  [HIGH] Host paths exposed - System structure revealed")
            risk_score += 5
        if self.results['uuids']:
            print("  [MEDIUM] UUIDs exposed - Session tracking possible")
            risk_score += 3
        if self.results['ip_addresses']:
            print("  [MEDIUM] IP addresses exposed - Network mapping possible")
            risk_score += 2
        
        print()
        print(f"  Overall Risk Score: {risk_score}/35")
        if risk_score >= 20:
            print("  🔴 CRITICAL - Immediate action required!")
        elif risk_score >= 10:
            print("  🟠 HIGH - Urgent patching needed")
        else:
            print("  🟡 MEDIUM - Schedule patching")
        print()
    
    def export_json(self, output_file):
        """Export results to JSON"""
        try:
            with open(output_file, 'w') as f:
                json.dump(dict(self.results), f, indent=2)
            print(f"✅ Results exported to {output_file}")
        except Exception as e:
            print(f"❌ Export failed: {e}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 analyze_mongobleed_leak.py <leaked.bin> [output.json]")
        sys.exit(1)
    
    analyzer = LeakedDataAnalyzer(sys.argv[1])
    analyzer.load_data()
    analyzer.analyze_all()
    analyzer.print_results()
    
    if len(sys.argv) > 2:
        analyzer.export_json(sys.argv[2])

if __name__ == "__main__":
    main()
