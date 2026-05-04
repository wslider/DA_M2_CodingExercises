import requests
import time

baseurl = 'https://rickandmortyapi.com/api/'
endpoint = 'character'

def main_request(baseurl, endpoint, page):
    url = f"{baseurl}{endpoint}?page={page}"
    try:
        r = requests.get(url, timeout=15)
        print(f"Page {page} → Status: {r.status_code} | Size: {len(r.text)} bytes")
        
        if r.status_code != 200:
            print(f"❌ Error {r.status_code}: {r.text[:300]}")
            return None
        
        return r.json()                     # only try json if status is 200
    except requests.exceptions.RequestException as e:
        print(f"❌ Request failed for page {page}: {e}")
        return None
    except Exception as e:
        print(f"❌ JSON decode failed for page {page}: {e}")
        print("Raw response:", r.text[:500])
        return None


def get_pages(response):
    return response['info']['pages']


def parse_json(response):
    charlist = []
    for item in response['results']:
        char = {
            "name": item['name'],
            "no_ep": len(item['episode']),
        }
        charlist.append(char)
    return charlist


# ===================== MAIN =====================
main_list = []

print("Fetching page 1 to get total pages...")
data = main_request(baseurl, endpoint, 1)

if not data:
    print("Cannot continue - first page failed")
else:
    total_pages = get_pages(data)
    print(f"Total pages: {total_pages}\n")

    for x in range(1, total_pages + 1):
        page_data = main_request(baseurl, endpoint, x)
        
        if page_data:
            chars = parse_json(page_data)
            main_list.extend(chars)
            print(f"Page {x}: +{len(chars)} characters")
        else:
            print(f"Page {x}: Skipped")
        
        time.sleep(0.4)   # Be gentle with the API

    print(f"\n🎉 Finished! Total characters: {len(main_list)}")
