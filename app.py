import gspread
import mapping

gc = gspread.oauth()
sh = gc.open("Rental Property Calculator")
wrks = sh.worksheets()

getField = [mapping.letters[x] for x in mapping.letters]
convertField = mapping.cellmapping[getField]

def setsheet(name): 
    for sheet in wrks: 
        if name in sheet.title: 
            worksheet =  sh.worksheet(sheet.title)
            return worksheet


#setsheet("Keshawn PDF")
            

def setfunctions(): 
    keyList = mapping.functionMapping.keys() 
    print(keyList)

#setfunctions()

def setAllValues(row_num, name):
    def get_rpq_vals(row_num, name): 
        rpq_col = [] 

        for key in mapping.functionMapping.keys():
            rpq_columns = (map(lambda letter: letter + row_num, mapping.letters))

        rpq_col.append(rpq_columns)

        return rpq_col
    
    getDisplay = [setsheet("RPQ").acell(x).value for x in get_rpq_vals(row_num, name)]

def newSheet(name): 
    sheet = sh.add_worksheet(name)
    for key, value in mapping.nameMapping.items():
        sheet.acell(key).update_acell(value)
    
    for key, value in mapping.colorMapping.items(): 
        sheet.format(key, {
            "backgroundColor": {
                key: value,
            }
        })
    
    for key, value in mapping.textClr.items(): 
        sheet.format(key, {
            "textFormat": {
                "foregroundColor": {
                    key: value,
                }
            },
            "bold": True
        })


