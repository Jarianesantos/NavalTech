# -*- coding: utf-8 -*-
"""
Script Python para gerar a seção de projetos do portfólio
"""

# Dados dos projetos com detalhes completos (projetos reais do GitHub)
projetos = [
    {
        "titulo": "NavalTech Platform",
        "categoria": "Sistema Web",
        "descricao": "Plataforma completa para prestação de serviços navais e tecnologia da IA com interface moderna.",
        "detalhes": "Portfólio profissional desenvolvido com Node.js, Express e HTML5/CSS3. Inclui sistema de autenticação, notificações por email e design responsivo inspirado no setor marítimo.",
        "tecnologias": ["Node.js", "Express", "HTML5", "CSS3"],
        "icon": "fas fa-ship",
        "link": "https://github.com/Jarianesantos/NavalTech",
        "funcionalidades": ["Sistema de autenticação", "Notificações por email", "Design responsivo", "Tema marítimo"]
    },
    {
        "titulo": "IANaval - Monitoramento Preditivo",
        "categoria": "Inteligência Artificial",
        "descricao": "Sistema de monitoramento preditivo de motor naval com sensores e rede neural.",
        "detalhes": "Projeto Python para detectar risco de falha em motor naval a partir de leituras de sensores (temperatura, pressão, vibração). Utiliza Pipeline do scikit-learn com StandardScaler e MLPClassifier.",
        "tecnologias": ["Python", "scikit-learn", "Pandas", "NumPy"],
        "icon": "fas fa-brain",
        "link": "https://github.com/Jarianesantos/ianaval",
        "funcionalidades": ["Análise preditiva", "Simulação em tempo real", "Diagnóstico automático", "Treinamento de modelo"]
    },
    {
        "titulo": "SeaGuardian - Monitoramento IA",
        "categoria": "Inteligência Artificial",
        "descricao": "Sistema de monitoramento marítimo baseado em inteligência artificial.",
        "detalhes": "Plataforma de monitoramento que utiliza IA para análise de dados marítimos,提供endo insights em tempo real sobre operações portuárias e de navegação.",
        "tecnologias": ["Python", "TensorFlow", "OpenCV", "Flask"],
        "icon": "fas fa-eye",
        "link": "https://github.com/Jarianesantos/seaguardian",
        "funcionalidades": ["Monitoramento em tempo real", "Análise de imagens", "Alertas automáticos", "Dashboard interativo"]
    },
    {
        "titulo": "PSV Hybrid Propulsion",
        "categoria": "Sistemas Embarcados",
        "descricao": "Sistema de propulsão híbrida para o PSV World Diamond.",
        "detalhes": "Desenvolvimento de sistema de gerenciamento energético para propulsão híbrida diesel-elétrica, otimizando consumo de combustível e reduzindo emissões.",
        "tecnologias": ["Python", "Arduino", "Sensores", "IoT"],
        "icon": "fas fa-cogs",
        "link": "https://github.com/Jarianesantos/psv-hybrid-propulsion",
        "funcionalidades": ["Gerenciamento energético", "Otimização de consumo", "Monitoramento de sensores", "Controle automático"]
    },
    {
        "titulo": "OptimarineAI",
        "categoria": "Inteligência Artificial",
        "descricao": "Algoritmos de otimização e redução de carbono para operações marítimas.",
        "detalhes": "Projeto de pesquisa focado em aplicar técnicas de IA e algoritmos de otimização para reduzir a emissão de carbono em embarcações, contribuindo para a sustentabilidade do setor naval.",
        "tecnologias": ["Python", "TensorFlow", "Algoritmos Genéticos", "Simulação"],
        "icon": "fas fa-leaf",
        "link": "https://github.com/Jarianesantos/optimarineAI",
        "funcionalidades": ["Otimização de rotas", "Redução de emissões", "Simulação ambiental", "Relatórios de sustentabilidade"]
    },
    {
        "titulo": "Maritime Data Platform",
        "categoria": "Ciência de Dados",
        "descricao": "Plataforma de dados marítimos com boias, territórios e infraestrutura portuária.",
        "detalhes": "Repositório de dados marítimos padronizados incluindo informações sobre boias, territórios marítimos, capitanias portuárias, dutos submarinos e outras infraestruturas relevantes.",
        "tecnologias": ["Python", "GeoPandas", "PostgreSQL", "QGIS"],
        "icon": "fas fa-database",
        "link": "https://github.com/Jarianesantos/maritime",
        "funcionalidades": ["Dados geoespaciais", "Análise territorial", "Visualização de mapas", "Exportação de dados"]
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