# -*- coding: utf-8 -*-
"""
Script Python para gerar a seção de projetos do portfólio
"""

# Dados dos projetos
projetos = [
    {
        "titulo": "NavalTech Platform",
        "categoria": "Sistema Web",
        "descricao": "Plataforma completa para gestão de operações marítimas com rastreamento em tempo real de embarcações e monitoramento de status.",
        "tecnologias": ["Node.js", "React", "PostgreSQL"],
        "icon": "fas fa-ship",
        "link": "#"
    },
    {
        "titulo": "Data Analytics API",
        "categoria": "API REST",
        "descricao": "API robusta para processamento e análise de dados com relatórios automatizados e integração com múltiplas fontes.",
        "tecnologias": ["Python", "FastAPI", "Redis"],
        "icon": "fas fa-chart-line",
        "link": "#"
    },
    {
        "titulo": "NavalTrack App",
        "categoria": "Mobile",
        "descricao": "Aplicativo mobile para rastreamento de embarcações e gestão de tripulações com notificações em tempo real.",
        "tecnologias": ["React Native", "Firebase", "Maps API"],
        "icon": "fas fa-mobile-alt",
        "link": "#"
    },
    {
        "titulo": "Marine Shop",
        "categoria": "E-commerce",
        "descricao": "Plataforma de e-commerce para equipamentos navais com pagamento integrado e gestão de estoque.",
        "tecnologias": ["Next.js", "Stripe", "MongoDB"],
        "icon": "fas fa-shopping-cart",
        "link": "#"
    },
    {
        "titulo": "Port Management System",
        "categoria": "Sistema Web",
        "descricao": "Sistema de gestão portuária para controle de cargas, agendamento de navios e acompanhamento operacional.",
        "tecnologias": ["Django", "React", "PostgreSQL"],
        "icon": "fas fa-warehouse",
        "link": "#"
    },
    {
        "titulo": "Weather Alert API",
        "categoria": "API REST",
        "descricao": "API de alertas meteorológicos para o setor marítimo com previsões personalizadas e notificações automáticas.",
        "tecnologias": ["Node.js", "Express", "MongoDB"],
        "icon": "fas fa-cloud-sun",
        "link": "#"
    }
]

def gerar_html_projetos():
    """Gera o HTML da seção de projetos"""
    
    html_projetos = ""
    
    for projeto in projetos:
        tecnologias_html = ""
        for tech in projeto["tecnologias"]:
            tecnologias_html += f'<span>{tech}</span>\n'
        
        html_projetos += f'''
      <article class="project-card">
        <div class="project-image">
          <div class="project-placeholder">
            <i class="{projeto["icon"]}"></i>
          </div>
          <div class="project-overlay">
            <a href="{projeto["link"]}" class="project-link">Ver Detalhes</a>
          </div>
        </div>
        <div class="project-info">
          <span class="project-category">{projeto["categoria"]}</span>
          <h3>{projeto["titulo"]}</h3>
          <p>{projeto["descricao"]}</p>
          <div class="project-tech">
            {tecnologias_html}
          </div>
        </div>
      </article>
'''
    
    return html_projetos

def gerar_secao_completa():
    """Gera a seção completa de projetos"""
    
    projetos_html = gerar_html_projetos()
    
    secao = f'''<!-- Projetos -->
<section class="section" id="projetos">
  <div class="container">
    <div class="section-header">
      <span class="section-tag">Portfólio</span>
      <h2 class="section-title">Projetos em Destaque</h2>
      <p class="section-subtitle">Conheça alguns dos meus trabalhos</p>
    </div>
    <div class="projects-grid">
{projetos_html}
    </div>
  </div>
</section>'''
    
    return secao

def salvar_html(arquivo_saida):
    """Salva o HTML gerado em um arquivo"""
    
    secao = gerar_secao_completa()
    
    with open(arquivo_saida, 'w', encoding='utf-8') as f:
        f.write(secao)
    
    print(f"HTML gerado e salvo em: {arquivo_saida}")
    print(f"Total de projetos: {len(projetos)}")

if __name__ == "__main__":
    print("Gerador de Projetos do Portfolio")
    print("=" * 40)
    
    # Lista os projetos
    print("\nProjetos configurados:")
    for i, projeto in enumerate(projetos, 1):
        print(f"  {i}. {projeto['titulo']} ({projeto['categoria']})")
    
    # Gera o HTML
    print("\nGerando HTML...")
    salvar_html("projetos_gerados.html")
    
    # Mostra preview
    print("\nPreview do HTML gerado:")
    print("-" * 40)
    secao = gerar_secao_completa()
    print(secao[:500] + "...")
    print("-" * 40)
    
    print("\nPronto! O arquivo projetos_gerados.html foi criado.")