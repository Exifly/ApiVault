from datetime import datetime
import xml.etree.ElementTree as ET

# legge gli URL dal file
with open('urls.txt', 'r') as f:
    urls = f.read().splitlines()

# crea un nuovo oggetto ElementTree
urlset = ET.Element('urlset')
urlset.set('xmlns', 'http://www.sitemaps.org/schemas/sitemap/0.9')

# per ogni URL, crea un nuovo elemento url e aggiungi loc e lastmod
for url in urls:
   url_elem = ET.SubElement(urlset, 'url')
   loc_elem = ET.SubElement(url_elem, 'loc')
   loc_elem.text = url
   lastmod_elem = ET.SubElement(url_elem, 'lastmod')
   lastmod_elem.text = datetime.now().strftime('%Y-%m-%d')
   priority_el = ET.SubElement(url_elem, 'priority')
   priority_el.text = "0.2"

# crea il file sitemap.xml e scrive l'ElementTree al suo interno
ET.ElementTree(urlset).write('sitemap.xml', encoding='utf-8', xml_declaration=True)