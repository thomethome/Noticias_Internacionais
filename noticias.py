import feedparser

# 🌎 Lista de feeds RSS focados em meio ambiente e sustentabilidade
feeds = [
    # Fontes Governamentais
    "https://www.gov.br/mma/pt-br/rss.xml",  # Ministério do Meio Ambiente (Brasil)
    "https://www.epa.gov/newsroom/rss.xml",  # Environmental Protection Agency (EUA)
    "https://www.eea.europa.eu/rss.xml",  # Agência Ambiental Europeia (Europa)
    
    # ONGs e Instituições Ambientais
    "https://www.wwf.org.br/rss.xml",  # WWF Brasil
    "https://feeds.feedburner.com/greenbiz",  # GreenBiz
    "https://www.nationalgeographic.com/environment/rss.xml",  # National Geographic Meio Ambiente
    "https://www.icmbio.gov.br/portal/rss/noticias",  # Instituto Chico Mendes (ICMBio)
    
    # Outras fontes ambientais
    "https://www.sciencedaily.com/rss/earth_climate.xml",  # Science Daily - Clima e Meio Ambiente
    "https://www.aljazeera.com/xml/rss/earth.xml",  # Al Jazeera - Meio Ambiente
    "https://rss.dw.com/rdf/rss-environment",  # Deutsche Welle (DW) - Meio Ambiente
]

def coletar_noticias():
    noticias = []
    
    for feed_url in feeds:
        feed = feedparser.parse(feed_url)
        
        for entrada in feed.entries[:10]:  # Pegando 10 notícias por feed
            titulo = entrada.title
            link = entrada.link
            
            # Filtrando manchetes relevantes com palavras-chave ambientais
            palavras_chave = ["sustentabilidade", "meio ambiente", "biodiversidade", "energia renovável", "conservação"]
            if any(palavra.lower() in titulo.lower() for palavra in palavras_chave):
                noticias.append(f"{titulo} - {link}")

    return noticias

# Salvar manchetes no arquivo
with open("manchetes.txt", "w", encoding="utf-8") as f:
    for noticia in coletar_noticias():
        f.write(noticia + "\n")

print("✅ Arquivo 'manchetes.txt' atualizado com notícias ambientais!")

 
