import httpx

with open("proxies.txt", 'w') as file:
	print("Proxies Scraper")
	file.write(httpx.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=anonymous").text)
	file.write(httpx.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt").text)
	file.write(httpx.get("https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt").text)
	file.write(httpx.get("https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt").text)
	file.write(httpx.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5").text)
	file.write(httpx.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5").text)
	file.write(httpx.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all&simplified=true").text)
	file.write(httpx.get("https://www.proxyscan.io/download?type=http").text)
	file.write(httpx.get("https://www.proxyscan.io/download?type=https").text)
	file.write(httpx.get("https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt").text)
	file.write(httpx.get("https://proxyspace.pro/http.txt").text)
	file.write(httpx.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=http").text)
	file.write(httpx.get("https://www.proxy-list.download/api/v1/get?type=http").text)
	file.write(httpx.get("https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt").text)