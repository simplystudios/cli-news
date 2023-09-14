from rich.console import Console
from rich.table import Table
import requests
console = Console()

data = requests.get("https://inshorts.me/news/top?offset=0&limit=10")
data1 = data.json()
num = 0
console.print(":newspaper:    _  __                 __      :newspaper:",justify="center", emoji= True,style="bold green")
console.print(":newspaper:   / |/ / __       __   ,'_/ /7() :newspaper:",justify="center", emoji= True,style="bold green")
console.print(":newspaper:  / || /,'o//7/7/7(c'  / /_ ///7  :newspaper:",justify="center", emoji= True,style="bold green")
console.print(":newspaper: /_/|_/ |_( |,^,'/__)  |__/////   :newspaper:",justify="center", emoji= True,style="bold green")
print(" ")



num = 0
table = Table(show_header=True, header_style="bold magenta")
table.add_column("Date", style="blue", width=12)
table.add_column("Title")
table.add_column("Author", justify="right")
table.add_column("Source", justify="right")
while num != 5:
    num = num + 1
    data2=data1["data"]["articles"][num]
    date = "Today"
    title = data2['title']
    auth = data2["authorName"]
    source = data2["sourceName"]
    table.add_row(
        date,
        title,
        auth,
        source,
        )
    if num == 5:
        console.print(table)    