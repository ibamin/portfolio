import requests
import re
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def find_emails_in_page(url):
    response = requests.get(url)
    content_text = response.text

    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    emails = re.findall(email_pattern, content_text)

    return emails


def crawl_for_emails(start_url, max_depth=1):
    visited = set()
    queue = [(start_url, 0)]

    while queue:
        url, depth = queue.pop(0)
        if depth > max_depth:
            break

        if url not in visited:
            try:
                emails = find_emails_in_page(url)
                print(f"Found {len(emails)} emails on {url}")
                for email in emails:
                    print(email)
                visited.add(url)

                response = requests.get(url)
                soup = BeautifulSoup(response.content, "html.parser")
                links = soup.find_all("a", href=True)
                for link in links:
                    next_url = urljoin(url, link["href"])
                    queue.append((next_url, depth + 1))
            except Exception as e:
                print(f"Error while processing {url}: {e}")


start_url = "https://www.hoseo.ac.kr/Home/Main.mbz"
crawl_for_emails(start_url, max_depth=2)
