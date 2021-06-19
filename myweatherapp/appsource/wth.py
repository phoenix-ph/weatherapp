from bs4 import BeautifulSoup
import requests
from tkinter import *
#آب و هوای شهر مورد نظر رو نشون میده.تاریخ طراحی هم 30/12/1399 هست.باز یادم باشه که این رو بروزرسانی کنم.





root =Tk()
root.title("هواشناسی ققنوس")
root.geometry('350x250')
root.configure(background="yellow")
cityNameLabel = Label(root, text='لطفا نام شهر خود را وارد کنید',font=("iransansdn",10))
cityNameLabel.pack()
cityNameEntry = Entry(root,bg='#595b83', fg='white', borderwidth=5, width=30,font=("iransansdn",10))
cityNameEntry.pack()
degreeLabel = Label(root, text='واحد دما',font=("iransansdn",10)).pack()
choosed = StringVar()
choosed.set('انتخاب')


def save():
    global city
    global value
    city = cityNameEntry.get()
    value = choosed.get()
    procces()

degreeMenu = OptionMenu(root, choosed, "سلسیوس", "فارنهایت")
degreeMenu.pack()

def procces():
    address = '''
    https://www.google.com/search?rlz=1C1CHBF_enIR891IR891&sxsrf=ALeKk03m9OMWKOC2j_DtHgAfvdyH4BmfXQ%3A1594136371743&ei=M5cEX-PtLMLikgXfmoGgCw&q=weather+{}+{}&oq=weather+{}+{}&gs_lcp=CgZwc3ktYWIQAzIECCMQJzIGCAAQCBAeMgYIABAIEB4yBggAEAgQHjIGCAAQCBAeUJFTWMBXYMhZaABwAHgAgAHgAYgB8QmSAQMyLTaYAQCgAQGqAQdnd3Mtd2l6&sclient=psy-ab&ved=0ahUKEwij06ThvLvqAhVCsaQKHV9NALQQ4dUDCAw&uact=5
    '''.format(city,value,city,value)
    source = requests.get(address)
    soup = BeautifulSoup(source.content, 'html.parser')
    global cityName, date, degree
    cityName = soup.find('span', class_='BNeawe tAd8D AP7Wnd')
    date = soup.find('div', class_='BNeawe tAd8D AP7Wnd')
    degree = soup.find('div', class_='BNeawe iBp4i AP7Wnd')
    status()
    


def myDelete():
    try:
        weatherStatus.destroy()
        
    except Exception:
        labelError.destroy()
    confirmButton['state']=NORMAL
    deleteButton['state']= DISABLED
        
            
def status():
    global weatherStatus
    try:
        weatherStatus = Label(root,font=("iransansdn",10), text="آب و هوا در {} on {} is {}".format(cityName.text,date.text,degree.text))
        weatherStatus.pack()
    except Exception:
        global labelError
        labelError= Label(root, text='شهر یافت نشد!',fg='red',font=("iransansdn",10))
        labelError.pack()
    confirmButton['state']=DISABLED
    deleteButton['state']= NORMAL
    
        

confirmButton = Button(root, text='تائید',bg="blue", fg='white', borderwidth=5, command=save,font=("iransansdn",8))
confirmButton.pack()
deleteButton = Button(root, text='حذف',bg="red", fg='white', borderwidth=5, command=myDelete,font=("iransansdn",8))
deleteButton.pack()
root.mainloop()