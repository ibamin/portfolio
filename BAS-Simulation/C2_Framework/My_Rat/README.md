# RAT
<p class="doc-hero">
  <img class="doc-hero-image" src="../../../assets/images/pexels-server-racks-5480781.jpg" alt="Server racks in a data center" />
  <span class="doc-hero-caption">Image: Brett Sayles / Pexels</span>
</p>
## 구조 다이어그램

```mermaid
flowchart TD
    Operator["Operator"] --> Server["C2 Server"]
    Server --> Agent["Agent"]
    Agent --> Host["Target Host"]
    Host --> Telemetry["Telemetry"]
    Telemetry --> Report["RAT"]
```

Rat Testing
