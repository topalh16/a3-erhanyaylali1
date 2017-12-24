#####################################################################
#####################################################################
### Assignment skeleton
### You can alter the below code to make your own dynamic website.
### The landing page for assignment 3 should be at /
#####################################################################

from bottle import route, run, default_app, debug, request

import csv

contents = []
with open("a2_input.csv") as input_file:
    for row in csv.reader(input_file):
        contents = contents + [row]


def htmlify(title, text):
    page = """
        <!doctype html>
        <html lang="en">
            <head>
                <meta charset="utf-8" />
                <title>%s</title>
                <style>
                    body{
                        background-image: url("http://all4desktop.com/data_images/original/4236715-wallpaper-background.jpg");

                        text-align : left;
                    }
                    p{
                text-align:left;
                color: #254117;
                font: New Times Roman;
                margin-left:2%%;
                font-size: 18px;
             }
                    select{
				width:40%%;
				text-align:left;
			}
                    table{
				margin-left:15%%;
				margin-right:15%%  ;
				border : 2 px solid black;
				width : 50%%;

			}
                    th{
				height : 50px;
				background-color : #26c6da;
				color : white;
			}
				    td{
				background-color : #26c6da;
				color : white;				    
			}
			    fieldset{
            padding-top: 8px;
            padding-left: 20px;
            padding-bottom: 20px;
            margin-left:70%%;
            margin-right:10%%;
            color:white;
            
            }
            </style>
            <body>
            <p>Best Selling Games designed by Erhan YAYLALI</p>
            %s
            </body>
        </html>

    """ % (title, text)
    return page


def index():
    text = """
		<br>
		<br>
		<br>
		<br>
		<br>
		<form action="/gamelist" method="POST">
	                <select name="game">
	                    <option value="1">Tetris</option>
	                    <option value="2">Minecraft</option>
	                    <option value="3">Wii Sports</option>
	                    <option value="4">Grand Theft Auto 5</option>
	                    <option value="5">Mario Kart Wii</option>
	                    <option value="6">Wii Sports Resort</option>
	                    <option value="7">Super Mario Bros</option>
	                    <option value="8">The Elder Scrolls V: Skyrim</option>
	                    <option value="9">Diablo III</option>
	                    <option value="10">New Super Mario Bros.</option>
	                    <option value="11">Wii Play</option>
	                    <option value="12">Grand Theft Auto: San Andreas</option>
	                    <option value="13">Call of Duty: Modern Warfare 3</option>
	                    <option value="14">Call of Duty: Black Ops</option>
	                    <option value="15">Grand Theft Auto IV</option>
	                    <option value="16">Overwatch</option>
	                    <option value="17">Call of Duty: Black Ops II</option>
	                    <option value="18">Kinect Adventures</option>
	                    <option value="19">Nintendogs</option>
	                    <option value="20">Pokemon Red and Blue</option>
	                    <option value="21">Mario Kart DS</option>
	                    <option value="22">Pokemon Gold and Silver</option>
	                    <option value="23">Wii Fit</option>
	                    <option value="24">Call of Duty: Modern Warfare 2</option>
	                    <option value="25">Wii Fit Plus 2009</option>
	                    <option value="26">Super Mario World</option>
	                    <option value="27">Battlefield 3</option>
	                    <option value="28">Grand Theft Auto: Vice City</option>
	                    <option value="29">The Sims 2</option>
	                    <option value="30">Terraria</option>
	                    <option value="31">Brain Age</option>
	                    <option value="32">Call of Duty: Ghosts</option>
	                    <option value="33">Super Mario Land</option>
	                    <option value="34">Pokemon Diamond and Pearl</option>
	                    <option value="35">Grand Theft Auto III</option>
	                    <option value="36">Super Mario Bros. 3</option>
	                    <option value="37">Pokemon Ruby and Sapphire</option>
	                    <option value="38">Pokemon X and Y</option>
	                    <option value="39">Need for Speed: Most Wanted</option>
	                    <option value="40">The Sims</option>
	                    <option value="41">Call of Duty 4: Modern Warfare</option>
	                    <option value="42">Call of Duty: World at War</option>
	                    <option value="43">Pokemon Black and White</option>
	                    <option value="44">Lemmings</option>
	                    <option value="45">Red Dead Redemption</option>
	                    <option value="46">Gran Tourismo 3</option>
	                    <option value="47">Super Mario Land</option>
	                </select>
	                <input type="submit" value="Search">
	    </form> 
	    <br>
	    <br>
	    <form action="/gamename" method="POST">
		<fieldset><legend>Searh by Name</legend>
		<br>	    
			<input type="textbox" name="gamename" placeholder="Search By Game Name"/>
			<input type="submit" value="Search">
		<br>
		</fieldset>
		</form>
	    <br>
	    <br>
	    <form action="/table" method="POST">
        <fieldset><legend>Year and Sales Statics</legend>
        <br>
                <input type="checkbox" name="table" value="1" >Year
                <input type="checkbox" name="table" value="2">Sales
                <input type="submit" value="Show All Column">
        </br>
        </fieldset>
        </form>
		<br>
		<br>
		<form action="/tops" method="POST">
        <fieldset><legend>Ranking</legend>
        <br>   
            <input type="radio" name="tops" value="2">Oldest Games</input>
            <input type="submit" value="Show">
        <br>
        </fieldset>
        </form>
	<br>
	<br>
		"""
    return htmlify("My lovely website", text)


def gamename():
    userinput = request.POST["gamename"]
    text = """<table border='2'>
                <tr>
                    <th>Game Name </th>
                    <th>Year </th>
                    <th>Sales </th>
                </tr>
        """
    for x in contents:
        if userinput in x[0]:
            text += """<tr>
                                <td>%(gamename)s</td>
                                <td>%(year)s</td>
                                <td>%(sales)s</td>
                            </tr>
                        """ % {"year": x[1], "gamename": x[0], "sales": x[2]}
    text += "</table>"
    return htmlify("Game Name", text)


def gamelist():
    a = request.POST['game']
    if a == "1":
        text = " Name: %s" \
               " Year: %s" \
               " Sales: %s"%(contents[2][0],contents[2][1],contents[2][2])
    elif a == "2":
        text = " Name: %s" \
               " Year: %s" \
               " Sales: %s" % (contents[3][0], contents[3][1], contents[3][2])
    elif a == "3":
        text = " Name: %s" \
               " Year: %s" \
               " Sales: %s" % (contents[4][0], contents[4][1], contents[4][2])
    elif a == "4":
        text = " Name: %s" \
               " Year: %s" \
               " Sales: %s" % (contents[5][0], contents[5][1], contents[5][2])
    elif a == "5":
        text = " Name: %s" \
               " Year: %s" \
               " Sales: %s" % (contents[6][0], contents[6][1], contents[6][2])
    elif a == "6":
        text = " Name: %s" \
               " Year: %s" \
               " Sales: %s" % (contents[7][0], contents[7][1], contents[7][2])
    elif a == "7":
        text = " Name: %s" \
               " Year: %s" \
               " Sales: %s" % (contents[8][0], contents[8][1], contents[8][2])
    elif a == "8":
        text = " Name: %s" \
               " Year: %s" \
               " Sales: %s" % (contents[9][0], contents[9][1], contents[9][2])
    elif a == "9":
        text = " Name: %s" \
               " Year: %s" \
               " Sales: %s" % (contents[10][0], contents[10][1], contents[10][2])
    elif a == "10":
        text = " Name: %s" \
               " Year: %s" \
               " Sales: %s" % (contents[11][0], contents[11][1], contents[11][2])
    elif a == "11":
        text = " Name: %s" \
               " Year: %s" \
               " Sales: %s" % (contents[12][0], contents[12][1], contents[12][2])
    elif a == "12":
        text = " Name: %s" \
               " Year: %s" \
               " Sales: %s" % (contents[13][0], contents[13][1], contents[13][2])
    elif a == "13":
        text = " Name: %s" \
               " Year: %s" \
               " Sales: %s" % (contents[14][0], contents[14][1], contents[14][2])
    elif a == "14":
        text = " Name: %s" \
               " Year: %s" \
               " Sales: %s" % (contents[15][0], contents[15][1], contents[15][2])
    elif a == "15":
        text = " Name: %s" \
               " Year: %s" \
               " Sales: %s" % (contents[16][0], contents[16][1], contents[16][2])
    elif a == "16":
        text = " Name: %s" \
               " Year: %s" \
               " Sales: %s" % (contents[17][0], contents[17][1], contents[17][2])
    elif a == "17":
        text = " Name: %s" \
               " Year: %s" \
               " Sales: %s" % (contents[18][0], contents[18][1], contents[18][2])
    elif a == "18":
        text = " Name: %s" \
               " Year: %s" \
               " Sales: %s" % (contents[19][0], contents[19][1], contents[19][2])
    elif a == "19":
        text = " Name: %s" \
               " Year: %s" \
               " Sales: %s" % (contents[20][0], contents[20][1], contents[20][2])
    elif a == "20":
        text = " Name: %s" \
               " Year: %s" \
               " Sales: %s" % (contents[21][0], contents[21][1], contents[21][2])
    elif a == "21":
        text = " Name: %s" \
               " Year: %s" \
               " Sales: %s" % (contents[22][0], contents[22][1], contents[22][2])
    elif a == "22":
        text = " Name: %s" \
               " Year: %s" \
               " Sales: %s" % (contents[23][0], contents[23][1], contents[23][2])
    elif a == "23":
        text = " Name: %s" \
               " Year: %s" \
               " Sales: %s" % (contents[24][0], contents[24][1], contents[24][2])
    elif a == "24":
        text = " Name: %s" \
               " Year: %s" \
               " Sales: %s" % (contents[25][0], contents[25][1], contents[25][2])
    elif a == "25":
        text = " Name: %s" \
               " Year: %s" \
               " Sales: %s" % (contents[26][0], contents[26][1], contents[26][2])
    elif a == "26":
        text = " Name: %s" \
               " Year: %s" \
               " Sales: %s" % (contents[27][0], contents[27][1], contents[27][2])
    elif a == "27":
        text = " Name: %s" \
               " Year: %s" \
               " Sales: %s" % (contents[28][0], contents[28][1], contents[28][2])
    elif a == "28":
        text = " Name: %s" \
               " Year: %s" \
               " Sales: %s" % (contents[29][0], contents[29][1], contents[29][2])
    elif a == "29":
        text = " Name: %s" \
               " Year: %s" \
               " Sales: %s" % (contents[30][0], contents[30][1], contents[30][2])
    elif a == "30":
        text = " Name: %s" \
               " Year: %s" \
               " Sales: %s" % (contents[31][0], contents[31][1], contents[31][2])
    elif a == "31":
        text = " Name: %s" \
               " Year: %s" \
               " Sales: %s" % (contents[32][0], contents[32][1], contents[32][2])
    elif a == "32":
        text = " Name: %s" \
               " Year: %s" \
               " Sales: %s" % (contents[33][0], contents[33][1], contents[33][2])
    elif a == "33":
        text = " Name: %s" \
               " Year: %s" \
               " Sales: %s" % (contents[34][0], contents[34][1], contents[34][2])
    elif a == "34":
        text = " Name: %s" \
               " Year: %s" \
               " Sales: %s" % (contents[35][0], contents[35][1], contents[35][2])
    elif a == "35":
        text = " Name: %s" \
               " Year: %s" \
               " Sales: %s" % (contents[36][0], contents[36][1], contents[36][2])
    elif a == "36":
        text = " Name: %s" \
               " Year: %s" \
               " Sales: %s" % (contents[37][0], contents[37][1], contents[37][2])
    elif a == "37":
        text = " Name: %s" \
               " Year: %s" \
               " Sales: %s" % (contents[38][0], contents[38][1], contents[38][2])
    elif a == "38":
        text = " Name: %s" \
               " Year: %s" \
               " Sales: %s" % (contents[39][0], contents[39][1], contents[39][2])
    elif a == "39":
        text = " Name: %s" \
               " Year: %s" \
               " Sales: %s" % (contents[40][0], contents[40][1], contents[40][2])
    elif a == "40":
        text = " Name: %s" \
               " Year: %s" \
               " Sales: %s" % (contents[41][0], contents[41][1], contents[41][2])
    elif a == "41":
        text = " Name: %s" \
               " Year: %s" \
               " Sales: %s" % (contents[42][0], contents[42][1], contents[42][2])
    elif a == "42":
        text = " Name: %s" \
               " Year: %s" \
               " Sales: %s" % (contents[43][0], contents[34][1], contents[43][2])
    elif a == "43":
        text = " Name: %s" \
               " Year: %s" \
               " Sales: %s" % (contents[44][0], contents[44][1], contents[44][2])
    elif a == "44":
        text = " Name: %s" \
               " Year: %s" \
               " Sales: %s" % (contents[45][0], contents[45][1], contents[45][2])
    elif a == "45":
        text = " Name: %s" \
               " Year: %s" \
               " Sales: %s" % (contents[46][0], contents[46][1], contents[46][2])
    elif a == "46":
        text = " Name: %s" \
               " Year: %s" \
               " Sales: %s" % (contents[47][0], contents[47][1], contents[47][2])
    elif a == "47":
        text = " Name: %s" \
               " Year: %s" \
               " Sales: %s" % (contents[48][0], contents[48][1], contents[48][2])
    return htmlify ("Game List", text)


def table():

    userinput = request.POST.getall("table")
    text ="""
        <table border='2'>
            <tr>
                <th>Game Name</th>"""
    for inpt in userinput:
        if  inpt == "1":
            text += """
                <th>Year</th>
                """
        elif inpt == "2":
            text += """
                <th>Sales</th>
                """
    text += """ </tr>\n"""
    for x in contents:
        if x[0] == "Best Selling Games Ever":
                    continue
        text += """<tr>
                    <td>%(gamename)s</td>"""%{"gamename":x[0]}
        for inpt in userinput:
            if inpt=="1":
                text += """
                        <td>%(year)s</td>
                    """%{"year":x[1]}
            elif inpt=="2":
                text += """
                        <td>%(sales)s</td>
                    """%{"sales":x[2]}
        text += """    </tr>\n"""
    text += """ </table>\n"""
    return htmlify("Game Table", text)

def tops():
    z = ""
    f = ""
    a = []
    if 'tops' in request.POST:
        tops = request.POST['tops']
    else:
        tops = ''

    if tops == "2":
        for i in range(1, 48):
            a += contents[i][1].split()
        b = sorted(set(a))
        for i in range(0, 21):
            c = b[i]
            for i in range(1, 48):
                if contents[i][1] == c:
                    z += """<tr><td>%(z)s</td><td>%(a)s</td><td>%(b)s</td></tr>""" % {"z": contents[i][0],
                                                                                      "a": contents[i][1],
                                                                                      "b": contents[i][2]}
        for j in range(0, 2):
            f += """<td>%s</td>""" % (contents[0][j])
    return htmlify("Rankings", '<table border="2">' + '<tr class="p">' + f + '<tr>' + z + '</table>')


route('/', 'GET', index)
route('/gamename', 'POST', gamename)
route('/gamelist', 'POST', gamelist)
route('/table', 'POST', table)
route('/tops', 'POST', tops)


#####################################################################
### Don't alter the below code.
### It allows this website to be hosted on Heroku
### OR run on your computer.
#####################################################################

# This line makes bottle give nicer error messages
debug(True)
# This line is necessary for running on Heroku
app = default_app()
# The below code is necessary for running this bottle app standalone on your computer.
if __name__ == "__main__":
    run()

