one = """<html>
            <head>
                <title>W E A T H E R</title>
                <link href='https://fonts.googleapis.com/css?family=Lato' rel='stylesheet'>"""

two ="""    </head>
            <body>
                <div>
                    <p><h1>The weather is probably</h1></p>
                    <img src="static/images/"""

three = """.svg"><p><h1>"""

four = """         </h1></p>
                </div>
            </body>
        </html>"""

style_one = """<style> div {
                    width: 80%;
                    text-align: center;
                    margin: 0 auto;
                    margin-top: 2em;
                } 

                @keyframes fadeBackground {
                    0% {
                        background-color: white;
                    }
                    100% {
                        background-color: """

style_two = """;     
                    }
                }

                body {
                    color: #696969;
                    font-family: 'Lato';
                    font-size: 18px;
                    animation: 1s ease 0s 1 fadeBackground;
                    animation-fill-mode: forwards;
                }</style>"""

def getBackgroundColorFromIcon(strIcon):
    if strIcon == '01d':    #clear sky
        return '#eedd82'
    elif strIcon == '01n':
        return '#191970'
    elif strIcon == '02d':  #few clouds
        return '#eee8aa'
    elif strIcon == '02n':
        return '#000080'
    elif strIcon == '03d' or strIcon == '03n':  #scattered clouds
        return '#d3d3d3'
    elif strIcon == '04d' or strIcon == '04n':  #broken clouds
        return '#778899'
    elif strIcon == '09d' or strIcon == '09n':  #shower rain
        return '#6a5acd'
    elif strIcon == '10d' or strIcon == '10n':  #rain
        return '#483d8b'
    elif strIcon == '11d' or strIcon == '11n':  #thunderstorm
        return '#fffacd'
    elif strIcon == '13d':  #snow
        return '#cdc9c9'
    elif strIcon == '13n':
        return '#8b8989'
    elif strIcon == '50d' or strIcon == '50n': #mist
        return '#b0e0e6'