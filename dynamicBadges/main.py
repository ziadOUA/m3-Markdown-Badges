import requests
from flask import Flask, Response

app = Flask(__name__, template_folder='templateFiles', static_folder='staticFiles')

# VARIANT 1 ----------------------------------------------------------------
variant_1 = ['#B02E26', '#974800', '#8E7500', '3F6900', '#4B6700', '#00696A', '#4B53B9', '#006493', '#8A33B8', '#9E2A99', '#99405E', '#1B1B1B']
on_variant_1 = '#FFF'

# VARIANT 2 ----------------------------------------------------------------
variant_2 = ['#FFB4AA', '#FFB689', '#E9C327', '#92DA35', '#AFD364', '#4CDADB', '#BEC2FF', '#8DCDFF', '#E8B3FF', '#FFABF1', '#FFB1C5', '#C6C6C6']
on_variant_2 = ['#690004', '#512400', '#3B2F00', '#1F3700', '#253600', '#003737', '#181F89', '#00344F', '#500075', '#5C005A', '#5E1130', '#303030']

# VARIANT 3 ----------------------------------------------------------------
variant_3 = ['#FFDAD5', '#FFDBC7', '#FFE177', '#ACF850', '#CAF07D', '#6FF6F7', '#E0E0FF', '#CAE6FF', '#F6D9FF', '#FFD7F4', '#FFD9E1', '#E2E2E2']
on_variant_3 = ['#410001', '#311300', '#231B00', '#102000', '#141F00', '#002020', '#00036B', '#001E30', '#310049', '#380037', '#3F001B', '#1B1B1B']

@app.route('/badge/stars/<style>/<variant>/<username>/<repo>')
def github_stars_badge(style, variant, username, repo):
    url = f'https://api.github.com/repos/{username}/{repo}'
    headers = {'Accept': 'application/vnd.github.v3+json'}
    r = requests.get(url, headers=headers)
    if r.ok:
        index = int(style) - 1

        if variant == '1':
            background = variant_1[index]
            foreground = on_variant_1
        if variant == '2':
            background = variant_2[index]
            foreground = on_variant_2[index]
        if variant == '3':
            background = variant_3[index]
            foreground = on_variant_3[index]

        data = r.json()
        stars = data['stargazers_count']

        if len(str(stars)) == 1:
            width = 20 + 68
        elif len(str(stars)) == 2:
            width = 2 * 16 + 68
        elif len(str(stars)) == 3:
            width = 3 * 14 + 68
        elif len(str(stars)) == 4:
            width = 4 * 13 + 68
        else:
            width = len(str(stars)) * 13 + 68
        
        svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="30" fill="{background}" rx="15"><path d="M40 0h4v20h-4z" fill="#4c1"/><rect rx="15" width="{width}" height="30" fill="{background}"/><text x="11" y="22" fill="{foreground}" font-size="20" font-family="Product Sans">Stars : {stars}</text></svg>'
        return Response(svg, mimetype='image/svg+xml')
    else:
        return 'Error', r.status_code
