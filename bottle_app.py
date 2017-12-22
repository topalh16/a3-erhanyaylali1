
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

def htmlify(title,text):
    page = """
        <!doctype html>
        <html lang="en">
            <head>
                <meta charset="utf-8" />
                <title>%s</title>
                <style>
                    select{
				width:50%%;
				text-align:center;
			}
                    table{
				margin-left:15%%;
				margin-right:15%%  ;
				border : 2 px solid black;
				width : 50%%;
				
			}
                    th{
				height : 50px;
				background-color : #4CAF50;
				color : white;
			}
                </style>
            <body>
            %s
            </body>
        </html>

    """ % (title,text)
    return page


def index():
	text = """
	<form action="/gamename" method="POST">
		<input type="textbox" name="gamename" placeholder="Search By Game Name"/>
		<input type="submit" value="Search">
	</form>
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
	<br/>
	"""
	return htmlify("My lovely website",text)

def gamename():
    userinput = request.POST["gamename"]
    text ="""<table>
                <tr>
                    <th>Game Name </th>
                    <th>Year </th>
                    <th>Sales </th>
                </tr>
        """
    for x in contents :
            if userinput in x[0]:
                text += """<tr>
                                <td>%(gamename)s</td>
                                <td>%(year)s</td>
                                <td>%(sales)s</td>
                            </tr>
                        """ % {"year" : x[1], "gamename":x[0], "sales":x[2]}
    text += "</table>"
    return htmlify("Title", text)

def gamelist():
    a = request.POST['game']
    
    if a=="1":
        text=" Information about the game you chase\n %s"%(contents[2])
    elif a=="2":
        text="Seçtiğiniz oyuna ait bilgiler: %s"%(contents[3])
    elif a=="3":
        text="Seçtiğiniz oyuna ait bilgiler: %s"%(contents[4])
    elif a=="4":
        text="Seçtiğiniz oyuna it bilgiler: %s"%(contents[5])
    elif a=="5":
        text="Seçtiğiniz oyuna ait bilgiler: %s"%(contents[6])
    elif a=="6":
        text="Seçtiğiniz oyuna ait bilgiler: %s"%(contents[7])
    elif a=="7":
        text="Seçtiğiniz oyuna ait bilgiler: %s"%(contents[8])
    elif a=="8":
        text="Seçtiğiniz oyuna ait bilgiler: %s"%(contents[9])
    elif a=="9":
        text="Seçtiğiniz oyuna ait bilgiler: %s"%(contents[10])
    elif a=="10":
        text="Seçtiğiniz oyuna ait bilgiler: %s"%(contents[11])
    elif a=="11":
        text="Seçtiğiniz oyuna ait bilgiler: %s"%(contents[12])
    elif a=="12":
        text="Seçtiğiniz oyuna ait bilgiler: %s"%(contents[13])
    elif a=="13":
        text="Seçtiğiniz oyuna ait bilgiler: %s"%(contents[14])
    elif a=="14":
        text="Seçtiğiniz oyuna ait bilgiler: %s"%(contents[15])
    elif a=="15":
        text="Seçtiğiniz oyuna ait bilgiler: %s"%(contents[16])
    elif a=="16":
        text="Seçtiğiniz oyuna ait bilgiler: %s"%(contents[17])
    elif a=="17":
        text="Seçtiğiniz oyuna ait bilgiler: %s"%(contents[18])
    elif a=="18":
        text="Seçtiğiniz oyuna ait bilgiler: %s"%(contents[19])
    elif a=="19":
        text="Seçtiğiniz oyuna ait bilgiler: %s"%(contents[20])
    elif a=="20":
        text="Seçtiğiniz oyuna ait bilgiler: %s"%(contents[21])
    elif a=="21":
        text="Seçtiğiniz oyuna ait bilgiler: %s"%(contents[22])
    elif a=="22":
        text="Seçtiğiniz oyuna ait bilgiler: %s"%(contents[23])
    elif a=="23":
        text="Seçtiğiniz oyuna ait bilgiler: %s"%(contents[24])
    elif a=="24":
        text="Seçtiğiniz oyuna ait bilgiler: %s"%(contents[25])
    elif a=="25":
        text="Seçtiğiniz oyuna ait bilgiler: %s"%(contents[26])
    elif a=="26":
        text="Seçtiğiniz oyuna ait bilgiler: %s"%(contents[27])
    elif a=="27":
        text="Seçtiğiniz oyuna ait bilgiler: %s"%(contents[28])
    elif a=="28":
        text="Seçtiğiniz oyuna ait bilgiler: %s"%(contents[29])
    elif a=="29":
        text="Seçtiğiniz oyuna ait bilgiler: %s"%(contents[30])
    elif a=="30":
        text="Seçtiğiniz oyuna ait bilgiler: %s"%(contents[31])
    elif a=="31":
        text="Seçtiğiniz oyuna ait bilgiler: %s"%(contents[32])
    elif a=="32":
        text="Seçtiğiniz oyuna ait bilgiler: %s"%(contents[33])
    elif a=="33":
        text="Seçtiğiniz oyuna ait bilgiler: %s"%(contents[34])
    elif a=="34":
        text="Seçtiğiniz oyuna ait bilgiler: %s"%(contents[35])
    elif a=="35":
        text="Seçtiğiniz oyuna ait bilgiler: %s"%(contents[36])
    elif a=="36":
        text="Seçtiğiniz oyuna ait bilgiler: %s"%(contents[37])
    elif a=="37":
        text="Seçtiğiniz oyuna ait bilgiler: %s"%(contents[38])
    elif a=="38":
        text="Seçtiğiniz oyuna ait bilgiler: %s"%(contents[39])
    elif a=="39":
        text="Seçtiğiniz oyuna ait bilgiler: %s"%(contents[40])
    elif a=="40":
        text="Seçtiğiniz oyuna ait bilgiler: %s"%(contents[41])
    elif a=="41":
        text="Seçtiğiniz oyuna ait bilgiler: %s"%(contents[42])
    elif a=="42":
        text="Seçtiğiniz oyuna ait bilgiler: %s"%(contents[43])
    elif a=="43":
        text="Seçtiğiniz oyuna ait bilgiler: %s"%(contents[44])
    elif a=="44":
        text="Seçtiğiniz oyuna ait bilgiler: %s"%(contents[45])
    elif a=="45":
        text="Seçtiğiniz oyuna ait bilgiler: %s"%(contents[46])
    elif a=="46":
        text="Seçtiğiniz oyuna ait bilgiler: %s"%(contents[47])
    elif a=="47":
        text="Seçtiğiniz oyuna ait bilgiler: %s"%(contents[48])
    return(text)
    


                    
route('/', 'GET', index)
route('/gamename', 'POST', gamename)
route('/gamelist', 'POST', gamelist)

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

