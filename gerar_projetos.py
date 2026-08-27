# -*- coding: utf-8 -*-
"""
Script Python para gerar a seção de projetos do portfólio
"""

# Dados dos projetos com detalhes completos
projetos = [
    {
        "titulo": "NavalTech Platform",
        "categoria": "Sistema Web",
        "descricao": "Plataforma completa para gestão de operações marítimas com rastreamento em tempo real de embarcações e monitoramento de status.",
        "detalhes": "Sistema desenvolvido para empresas do setor marítimo que necessitam de controle total sobre suas operações. Inclui rastreamento GPS em tempo real, dashboard administrativo, relatórios automatizados e sistema de alertas.",
        "tecnologias": ["Node.js", "React", "PostgreSQL"],
        "icon": "fas fa-ship",
        "link": "#",
        "funcionalidades": ["Rastreamento GPS em tempo real", "Dashboard administrativo", "Relatórios automatizados", "Sistema de alertas"]
    },
    {
        "titulo": "Data Analytics API",
        "categoria": "API REST",
        "descricao": "API robusta para processamento e análise de dados com relatórios automatizados e integração com múltiplas fontes.",
        "detalhes": "API desenvolvida para empresas que precisam processar grandes volumes de dados. Oferece endpoints para inserção, consulta e análise de dados com geração de relatórios em PDF e Excel.",
        "tecnologias": ["Python", "FastAPI", "Redis"],
        "icon": "fas fa-chart-line",
        "link": "#",
        "funcionalidades": ["Processamento de dados em lote", "Geração de relatórios", "Cache com Redis", "Documentação Swagger"]
    },
    {
        "titulo": "NavalTrack App",
        "categoria": "Mobile",
        "descricao": "Aplicativo mobile para rastreamento de embarcações e gestão de tripulações com notificações em tempo real.",
        "detalhes": "Aplicativo desenvolvido para tripulantes e gestores de frota marítima. Permite acompanhar a posição das embarcações, receber alertas de изменения de rota e gerenciar escalas de tripulação.",
        "tecnologias": ["React Native", "Firebase", "Maps API"],
        "icon": "fas fa-mobile-alt",
        "link": "#",
        "funcionalidades": ["Mapa interativo", "Notificações push", "Gestão de tripulação", "Modo offline"]
    },
    {
        "titulo": "Marine Shop",
        "categoria": "E-commerce",
        "descricao": "Plataforma de e-commerce para equipamentos navais com pagamento integrado e gestão de estoque.",
        "detalhes": "Loja virtual completa para venda de equipamentos e suprimentos navais. Sistema de pagamento integrado, controle de estoque, gestão de pedidos e painel administrativo para vendedores.",
        "tecnologias": ["Next.js", "Stripe", "MongoDB"],
        "icon": "fas fa-shopping-cart",
        "link": "#",
        "funcionalidades": ["Pagamento integrado", "Gestão de estoque", "Painel admin", "Sistema de frete"]
    },
    {
        "titulo": "Port Management System",
        "categoria": "Sistema Web",
        "descricao": "Sistema de gestão portuária para controle de cargas, agendamento de navios e acompanhamento operacional.",
        "detalhes": "Sistema desenvolvido para portos que precisam gerenciar operações de carga e descarga. Inclui agendamento de navios, controle de cargas, acompanhamento em tempo real e relatórios operacionais.",
        "tecnologias": ["Django", "React", "PostgreSQL"],
        "icon": "fas fa-warehouse",
        "link": "#",
        "funcionalidades": ["Agendamento de navios", "Controle de cargas", "Dashboard operacional", "Relatórios automáticos"]
    },
    {
        "titulo": "Weather Alert API",
        "categoria": "API REST",
        "descricao": "API de alertas meteorológicos para o setor marítimo com previsões personalizadas e notificações automáticas.",
        "detalhes": "API que fornece dados meteorológicos personalizados para operações marítimas. Inclui previsões de ondas, ventos, visibilidade e alertas de tempestades com notificações automáticas.",
        "tecnologias": ["Node.js", "Express", "MongoDB"],
        "icon": "fas fa-cloud-sun",
        "link": "#",
        "funcionalidades": ["Previsão de ondas", "Alertas de tempestades", "Notificações automáticas", "Histórico meteorológico"]
    }
]

def gerar_html_projetos():
    """Gera o HTML da seção de projetos"""
    
    html_projetos = ""
    
    for projeto in projetos:
        tecnologias_html = ""
        for tech in projeto["tecnologias"]:
            tecnologias_html += f'<span>{tech}</span>\n'
        
        funcionalidades_html = ""
        for func in projeto["funcionalidades"]:
            funcionalidades_html += f'<li>{func}</li>\n'
        
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
          <p class="project-details">{projeto["detalhes"]}</p>
          <div class="project-features">
            <h4>Funcionalidades:</h4>
            <ul>
              {funcionalidades_html}
            </ul>
          </div>
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