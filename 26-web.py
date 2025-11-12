# ==========================================================
# 30 Days of Python - Day 26: Python Web com Flask
# ==========================================================
# O objetivo deste dia é introduzir o desenvolvimento web em Python
# usando o framework Flask — um microframework leve e flexível.
#
# ----------------------------------------------------------
# 1. O que é o Flask
# ----------------------------------------------------------
# - É um microframework web escrito em Python.
# - Considerado “micro” porque fornece apenas o essencial:
#   servidor web, sistema de rotas e suporte a templates (Jinja2).
# - Permite criar rapidamente aplicações web e APIs RESTful.
# - É ideal para projetos pequenos ou médios, ou quando se quer
#   ter controle total sobre a estrutura da aplicação.
#
# ----------------------------------------------------------
# 2. Estrutura básica de uma aplicação Flask
# ----------------------------------------------------------
# - app = Flask(__name__) → cria a aplicação.
# - @app.route("/") → define uma rota (endpoint) que o servidor atende.
# - def função(): → função associada à rota (view function).
# - app.run(debug=True) → executa o servidor local de desenvolvimento.
#
# Exemplo conceitual:
#     from flask import Flask
#     app = Flask(__name__)
#
#     @app.route("/")
#     def home():
#         return "Hello, Flask!"
#
#     if __name__ == "__main__":
#         app.run(debug=True)
#
# ----------------------------------------------------------
# 3. Rotas e métodos HTTP
# ----------------------------------------------------------
# - Uma rota é associada a um caminho (URL) e a uma função.
# - Cada rota pode aceitar diferentes métodos HTTP:
#     GET (padrão): consulta
#     POST: envio de dados (formulários, JSON)
#     PUT, DELETE, PATCH: operações mais avançadas (REST)
#
# - Parâmetros podem ser passados:
#     • Diretamente na URL → /hello/<name>
#     • Via query string → /sum?a=10&b=20
#     • Via corpo (POST JSON) → request.get_json()
#
# ----------------------------------------------------------
# 4. Retornos
# ----------------------------------------------------------
# - A função associada à rota pode retornar:
#     • Texto simples (string)
#     • HTML (renderizado manualmente ou com templates Jinja2)
#     • JSON (usando jsonify)
#
# - jsonify transforma dicionários Python em JSON automaticamente.
# - O Flask também permite definir códigos de status (200, 404, 500, etc.).
#
# ----------------------------------------------------------
# 5. Templates (Jinja2)
# ----------------------------------------------------------
# - Flask utiliza o mecanismo de templates Jinja2.
# - Permite criar páginas HTML dinâmicas com tags de controle:
#     {{ variável }} → exibe valores
#     {% comando %} → estruturas de controle (for, if, etc.)
# - Os arquivos HTML ficam normalmente em uma pasta "templates".
# - Exemplo de uso:
#     from flask import render_template
#     return render_template("index.html", name="Isabella")
#
# ----------------------------------------------------------
# 6. API e JSON
# ----------------------------------------------------------
# - Flask pode ser usado para construir APIs REST.
# - request → objeto que contém dados da requisição:
#     request.args → parâmetros da URL
#     request.get_json() → corpo JSON
# - jsonify → retorna resposta JSON estruturada.
# - Ideal para back-ends que se comunicam com front-ends React, Vue etc.
#
# ----------------------------------------------------------
# 7. Modo debug e ambiente de desenvolvimento
# ----------------------------------------------------------
# - app.run(debug=True) ativa o “debug mode”:
#     • recarrega automaticamente o servidor quando o código muda
#     • exibe erros com detalhes úteis
# - Para produção, usa-se servidores WSGI (Gunicorn, uWSGI, etc.).
#
# ----------------------------------------------------------
# 8. Estrutura típica de projeto Flask
# ----------------------------------------------------------
# projeto/
# ├─ app.py               → ponto de entrada
# ├─ templates/           → páginas HTML
# ├─ static/              → CSS, JS, imagens
# └─ requirements.txt     → dependências
#
# ----------------------------------------------------------
# 9. Flask x Django
# ----------------------------------------------------------
# - Flask é minimalista e flexível; Django é completo e opinativo.
# - Flask dá liberdade de escolha de bibliotecas (ORM, autenticação, etc.).
# - Django já traz tudo pronto (ORM, admin, autenticação, formulários).
# - Flask é ideal para APIs pequenas e microserviços;
#   Django é ótimo para sistemas maiores e estruturados.
#
# ----------------------------------------------------------
# 10. Conceitos complementares abordados
# ----------------------------------------------------------
# - Ambiente virtual (venv) para isolar dependências.
# - Requisições HTTP e ciclo request → response.
# - Estrutura MVC (Model–View–Controller) simplificada:
#     • Model: camada de dados (opcional ou com SQLAlchemy)
#     • View: funções e templates
#     • Controller: lógica de requisição e resposta
# - Boas práticas:
#     • usar blueprints para modularizar
#     • separar lógica de rotas e templates
#     • usar variáveis de ambiente para configurações
#
# ----------------------------------------------------------
# Conclusão
# ----------------------------------------------------------
# O Day 26 mostra os fundamentos do desenvolvimento web com Flask:
# como servir páginas, criar rotas, lidar com requisições,
# responder em HTML e JSON e estruturar uma aplicação básica.
# A partir daqui, o próximo passo (Day 27) é aprender Django,
# um framework completo com ORM, sistema de templates e painel administrativo.
# ==========================================================
