#! /usr/bin/env python
__author__ = 'Rajesh Majumdar'

try:
    from tkinter import *
    import tkinter.scrolledtext as sctx
except:
    from Tkinter import *
    import ScrolledText as sctx


try:
    import ttk
except ImportError:
    from tkinter.ttk import ttk

import atexit
import os
import sys


from aboutme import aboutme
from contact import contact
from about import about
from licenses import licenses
from updates import checkupdates
from suggestions import suggestions
from contributors import contributions
from checktool import checktool
from mydownloads import mydownloads
from savedownloads import  startdownload, savedownloads
from report import report

def hello():
    print 'hello world'

def atgexit():
    try:
        os.remove('mydownloads.txt')
    except:
        pass

def mainbody():

    root = Tk()

    root.geometry("577x556+427+139")
    root.title("PloitKit - The Hacker's Toolbox")
    root.configure(background="#d9d9d9")
    #root.wm_iconbitmap('images/icon.ico')
    #root.resizable(0,0)

    imagepath = r'images/header.gif'
    image = PhotoImage(file=imagepath)
    ilabel = Label(root, image = image)
    ilabel.image = image
    ilabel.pack()

    varinfo = StringVar(root, value='Information Gathering')
    varvuln = StringVar(root, value="Vulnerability Analysis")
    varexploit = StringVar(root, value="Exploitation Tool")
    varwireless = StringVar(root, value="Wireless Attacks")
    varforensic = StringVar(root, value="Forensics Tools")
    varwebapp = StringVar(root, value="Web Application")
    varstress = StringVar(root, value="Stress Testing")
    varsniff = StringVar(root, value="Sniffing & Spoofing")
    varpass = StringVar(root, value="Password Attacks")
    varhard = StringVar(root, value="Hardware Hacking")
    varreverse = StringVar(root, value="Reverse Engineering")
    varreport = StringVar(root, value="Reporting tools")
    varall = StringVar(root, value="All tools")

    infolist = 'acccheck','ace-voip','Amap','Automater','bing-ip2hosts','braa','CaseFile','CDPSnarf','cisco-torch','Cookie Cadger','copy-router-config','DMitry','dnmap','dnsenum','dnsmap','DNSRecon','dnstracer','dnswalk','DotDotPwn','enum4linux','enumIAX','Fierce','Firewalk','fragroute','fragrouter','Ghost Phisher','GoLismero','goofile','hping3','InTrace','iSMTP','lbd','Maltego Teeth','masscan','Metagoofil','Miranda','nbtscan-unixwiz','Nmap','ntop','p0f','Parsero','Recon-ng','SET','smtp-user-enum','snmp-check','sslcaudit','SSLsplit','sslstrip','SSLyze','THC-IPV6','theHarvester','TLSSLed','twofi','URLCrazy','Wireshark','WOL-E','Xplico'
    vulnlist = 'BBQSQL','BED','BruteXSS','cisco-auditing-tool','cisco-global-exploiter','cisco-ocs','cisco-torch','copy-router-config','DBPwAudit','Doona','DotDotPwn','Greenbone Security Assistant','GSD','HexorBase','Inguma','jSQL','Lynis','Nmap','ohrwurm','openvas-administrator','openvas-cli','openvas-manager','openvas-scanner','Oscanner','Powerfuzzer','sfuzz','SidGuesser','SIPArmyKnife','sqlmap','Sqlninja','sqlsus','THC-IPV6','tnscmd10g','unix-privesc-check','Yersinia'
    exploitlist = 'Armitage','Backdoor Factory','BeEF','cisco-auditing-tool','cisco-global-exploiter','cisco-ocs','cisco-torch','Commix','crackle','exploitdb','jboss-autopwn','Linux Exploit Suggester','Maltego Teeth','SET','ShellNoob','sqlmap','struts pwn','THC-IPV6','Yersinia'
    wirelesslist = 'Aircrack-ng','Asleap','Bluelog','BlueMaho','Bluepot','BlueRanger','Bluesnarfer','Bully','coWPAtty','crackle','eapmd5pass','Fern Wifi Cracker','Ghost Phisher','GISKismet','Gqrx','gr-scan','hostapd-wpe','kalibrate-rtl','KillerBee','mdk3','mfcuk','mfoc','mfterm','Multimon-NG','PixieWPS','Reaver','redfang','RTLSDR Scanner','Spooftooph','Wifi Honey','wifiphisher','Wifitap','Wifite'
    forensiclist = 'Binwalk','bulk-extractor','Capstone','chntpw','Cuckoo','dc3dd','ddrescue','DFF','diStorm3','Dumpzilla','extundelete','Foremost','Galleta','Guymager','iPhone Backup Analyzer','p0f','pdf-parser','pdfid','pdgmail','peepdf','RegRipper','Volatility','Xplico'
    webapplist = 'apache-users','Arachni','BBQSQL','BlindElephant','Burp Suite','CutyCapt','DAVTest','deblaze','DIRB','DirBuster','fimap','FunkLoad','Gobuster','Grabber','jboss-autopwn','joomscan','jSQL','Maltego Teeth','PadBuster','Paros','Parsero','plecost','Powerfuzzer','ProxyStrike','Recon-ng','Skipfish','sqlmap','Sqlninja','sqlsus','ua-tester','Uniscan','Vega','w3af','WebScarab','Webshag','WebSlayer','WebSploit','Wfuzz','WPScan','XSSer','zaproxy'
    stresslist = 'DHCPig','FunkLoad','iaxflood','Inundator','inviteflood','ipv6-toolkit','mdk3','Reaver','rtpflood','SlowHTTPTest','t50','Termineter','THC-IPV6','THC-SSL-DOS'
    snifflist = 'Burp Suite','DNSChef','fiked','hamster-sidejack','HexInject','iaxflood','inviteflood','iSMTP','isr-evilgrade','mitmproxy','ohrwurm','protos-sip','rebind','responder','rtpbreak','rtpinsertsound','rtpmixsound','sctpscan','SIPArmyKnife','SIPp','SIPVicious','SniffJoke','SSLsplit','sslstrip','THC-IPV6','VoIPHopper','WebScarab','Wifi Honey','Wireshark','xspy','Yersinia','zaproxy'
    passlist = 'acccheck','Burp Suite','CeWL','chntpw','cisco-auditing-tool','CmosPwd','creddump','crunch','DBPwAudit','findmyhash','gpp-decrypt','hash-identifier','HexorBase','THC-Hydra','John the Ripper','Johnny','keimpx','Maltego Teeth','Maskprocessor','multiforcer','Ncrack','oclgausscrack','PACK','patator','phrasendrescher','polenum','RainbowCrack','rcracki-mt','RSMangler','SQLdict','Statsprocessor','THC-pptp-bruter','TrueCrack','WebScarab','wordlists','zaproxy'
    hardlist = 'android-sdk','apktool','Arduino','dex2jar','Sakis3G','smali'
    reverselist = 'apktool','dex2jar','diStorm3','edb-debugger','jad','javasnoop','JD-GUI','OllyDbg','smali','Valgrind','YARA'
    reportlist = 'CaseFile','CutyCapt','dos2unix','Dradis','KeepNote','MagicTree','Metagoofil','Nipper-ng','pipal'
    alllist = 'BruteXSS','dos2unix','Dradis','KeepNote','MagicTree','Metagoofil','Nipper-ng','pipal','diStorm3','edb-debugger','jad','javasnoop','JD-GUI','OllyDbg','Valgrind','YARA','acccheck','ace-voip','Amap','Automater','bing-ip2hosts','braa','CaseFile','CDPSnarf','Cookie Cadger','copy-router-config','DMitry','dnmap','dnsenum','dnsmap','DNSRecon','dnstracer','dnswalk','enum4linux','enumIAX','Fierce','Firewalk','fragroute','fragrouter','GoLismero','goofile','hping3','InTrace','lbd','masscan','Miranda','nbtscan-unixwiz','ntop','smtp-user-enum','snmp-check','sslcaudit','struts pwn','SSLyze','theHarvester','TLSSLed','twofi','URLCrazy','WOL-E','BED','cisco-global-exploiter','cisco-ocs','Doona','DotDotPwn','Greenbone Security Assistant','GSD','Inguma','Lynis','Nmap','openvas-administrator','openvas-cli','openvas-manager','openvas-scanner','Oscanner','sfuzz','SidGuesser','Sqlninja','sqlsus','tnscmd10g','unix-privesc-check','Yersinia','Armitage','Backdoor Factory','BeEF','cisco-auditing-tool','cisco-torch','Commix','crackle','exploitdb','Linux Exploit Suggester','SET','ShellNoob','Aircrack-ng','Asleap','Bluelog','BlueMaho','Bluepot','BlueRanger','Bluesnarfer','Bully','coWPAtty','eapmd5pass','Fern Wifi Cracker','Ghost Phisher','GISKismet','Gqrx','gr-scan','hostapd-wpe','kalibrate-rtl','KillerBee','mdk3','mfcuk','mfoc','mfterm','Multimon-NG','PixieWPS','redfang','RTLSDR Scanner','Spooftooph','wifiphisher','Wifitap','Wifite','Binwalk','bulk-extractor','Capstone','Cuckoo','dc3dd','ddrescue','DFF','Dumpzilla','extundelete','Foremost','Galleta','Guymager','iPhone Backup Analyzer','p0f','pdf-parser','pdfid','pdgmail','peepdf','RegRipper','Volatility','Xplico','apache-users','Arachni','BBQSQL','BlindElephant','Burp Suite','CutyCapt','DAVTest','deblaze','DIRB','DirBuster','fimap','Gobuster','Grabber','jboss-autopwn','joomscan','jSQL','PadBuster','Paros','Parsero','plecost','Powerfuzzer','ProxyStrike','Recon-ng','Skipfish','sqlmap','ua-tester','Uniscan','Vega','w3af','Webshag','WebSlayer','WebSploit','Wfuzz','WPScan','XSSer','DHCPig','FunkLoad','iaxflood','Inundator','inviteflood','ipv6-toolkit','Reaver','rtpflood','SlowHTTPTest','t50','Termineter','THC-SSL-DOS','DNSChef','fiked','hamster-sidejack','HexInject','iSMTP','isr-evilgrade','mitmproxy','ohrwurm','protos-sip','rebind','responder','rtpbreak','rtpinsertsound','rtpmixsound','sctpscan','SIPArmyKnife','SIPp','SIPVicious','SniffJoke','SSLsplit','sslstrip','THC-IPV6','VoIPHopper','Wifi Honey','Wireshark','xspy','CeWL','chntpw','CmosPwd','creddump','crunch','DBPwAudit','findmyhash','gpp-decrypt','hash-identifier','HexorBase','THC-Hydra','John the Ripper','Johnny','keimpx','Maltego Teeth','Maskprocessor','multiforcer','Ncrack','oclgausscrack','PACK','patator','phrasendrescher','polenum','RainbowCrack','rcracki-mt','RSMangler','SQLdict','Statsprocessor','THC-pptp-bruter','TrueCrack','WebScarab','wordlists','zaproxy','android-sdk','apktool','Arduino','dex2jar','Sakis3G','smali'
    alltools ='brutexss','dos2unix','dradis','keepnote','magictree','metagoofil','nipper-ng','pipal','distorm3','edb-debugger','jad','javasnoop','jd-gui','ollydbg','valgrind','yara','acccheck','ace-voip','amap','automater','bing-ip2hosts','braa','caseFile','cdpsnarf','cookie cadger','copy-router-config','dmitry','dnmap','dnsenum','dnsmap','dnsrecon','dnstracer','dnswalk','enum4linux','enumiax','fierce','firewalk','fragroute','fragrouter','golismero','goofile','hping3','intrace','lbd','masscan','miranda','nbtscan-unixwiz','ntop','smtp-user-enum','snmp-check','sslcaudit','struts pwn','sslyze','theharvester','tlssled','twofi','urlcrazy','wol-e','bed','cisco-global-exploiter','cisco-ocs','doona','dotdotpwn','greenbone security assistant','gsd','inguma','lynis','nmap','openvas-administrator','openvas-cli','openvas-manager','openvas-scanner','oscanner','sfuzz','sidguesser','sqlninja','sqlsus','tnscmd10g','unix-privesc-check','yersinia','armitage','backdoor factory','beef','cisco-auditing-tool','cisco-torch','commix','crackle','exploitdb','linux exploit suggester','set','shellnoob','aircrack-ng','asleap','bluelog','blueMaho','bluepot','blueranger','bluesnarfer','bully','cowpatty','eapmd5pass','fern wifi cracker','ghost phisher','giskismet','gqrx','gr-scan','hostapd-wpe','kalibrate-rtl','killerbee','mdk3','mfcuk','mfoc','mfterm','multimon-ng','pixiewps','redfang','rtlsdr scanner','spooftooph','wifiphisher','wifitap','wifite','binwalk','bulk-extractor','capstone','cuckoo','dc3dd','ddrescue','dff','dumpzilla','extundelete','foremost','galleta','guymager','iphone backup analyzer','p0f','pdf-parser','pdfid','pdgmail','peepdf','regripper','volatility','xplico','apache-users','arachni','bbqsql','blindelephant','burp suite','cutycapt','davtest','deblaze','dirb','dirbuster','fimap','gobuster','grabber','jboss-autopwn','joomscan','jsql','padbuster','paros','parsero','plecost','powerfuzzer','proxystrike','recon-ng','skipfish','sqlmap','ua-tester','uniscan','vega','w3af','webshag','webslayer','websploit','wfuzz','wpscan','xsser','dhcpig','funkload','iaxflood','Inundator','inviteflood','ipv6-toolkit','reaver','rtpflood','slowhttptest','t50','termineter','thc-ssl-dos','dnschef','fiked','hamster-sidejack','hexinject','ismtp','isr-evilgrade','mitmproxy','ohrwurm','protos-sip','rebind','responder','rtpbreak','rtpinsertsound','rtpmixsound','sctpscan','siparmyknife','sipp','sipvicious','sniffjoke','sslsplit','sslstrip','thc-ipv6','voiphopper','wifi honey','wireshark','xspy','cewl','chntpw','cmospwd','creddump','crunch','dbpwaudit','findmyhash','gpp-decrypt','hash-identifier','hexorbase','thc-hydra','john the ripper','johnny','keimpx','maltego teeth','maskprocessor','multiforcer','ncrack','oclgausscrack','pack','patator','phrasendrescher','polenum','rainbowcrack','rcracki-mt','rsmangler','sqldict','statsprocessor','thc-pptp-bruter','truecrack','webscarab','wordlists','zaproxy','android-sdk','apktool','arduino','dex2jar','sakis3g','smali'

    def downloadsection():

        def cbinfo_onEnter(event):

            #It will get the values
            cbinfovalue = format(cbinfo.get())
            cbvulnvalue = format(cbvuln.get())
            cbexploitvalue = format(cbexploit.get())
            cbwirelessvalue = format(cbwireless.get())
            cbforensicsvalue = format(cbforensics.get())
            cbwebvalue = format(cbweb.get())
            cbstressvalue = format(cbstress.get())
            cbsniffvalue = format(cbsniff.get())
            cbpassvalue = format(cbpass.get())
            cbhardvalue = format(cbhard.get())
            cbreversevalue = format(cbreverse.get())
            cbreportvalue = format(cbreport.get())
            cballvalue = format(cball.get())

            result = cbreportvalue+"\n"+cbinfovalue+"\n"+cbvulnvalue+"\n"+cbexploitvalue+"\n"+cbwirelessvalue+"\n"+cbforensicsvalue+"\n"+cbwebvalue+"\n"+cbstressvalue+"\n"+cbsniffvalue+"\n"+cbsniffvalue+"\n"+cbpassvalue+"\n"+cbhardvalue+"\n"+cbreversevalue+"\n"+cbreportvalue+"\n"+cballvalue
            #print result

            checktool(result)
            startdownload()


        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'
        style = ttk.Style()
        if sys.platform == "win32":
            style.theme_use('winnative')
        style.configure('.',background=_bgcolor)
        style.configure('.',foreground=_fgcolor)
        style.configure('.',font="TkDefaultFont")
        style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])


        #Information Gathering Drop Down
        cbinfo = ttk.Combobox( width=70, textvariable=varinfo)
        cbinfo.bind("<Return>", cbinfo_onEnter)
        cbinfo.bind("<<ComboboxSelected>>", cbinfo_onEnter)
        cbinfo['values']=(infolist)
        cbinfo.place(relx=0.115, rely=0.18)

        #Vulnerability Analysis Drop Down
        cbvuln = ttk.Combobox( width=70, textvariable=varvuln)
        cbvuln.bind("<Return>", cbinfo_onEnter)
        cbvuln.bind("<<ComboboxSelected>>", cbinfo_onEnter)
        cbvuln['values']=(vulnlist)
        cbvuln.place(relx=0.115, rely=0.24)

        #Exploitation Tool Drop Down
        cbexploit = ttk.Combobox( width=70, textvariable=varexploit)
        cbexploit.bind("<Return>", cbinfo_onEnter)
        cbexploit.bind("<<ComboboxSelected>>", cbinfo_onEnter)
        cbexploit['values']=(exploitlist)
        cbexploit.place(relx=0.115, rely=0.30)

        #Wireless Attacks Drop Down
        cbwireless = ttk.Combobox( width=70, textvariable=varwireless)
        cbwireless.bind("<Return>", cbinfo_onEnter)
        cbwireless.bind("<<ComboboxSelected>>", cbinfo_onEnter)
        cbwireless['values']=(wirelesslist)
        cbwireless.place(relx=0.115, rely=0.36)

        #Foresics tools Drop Down
        cbforensics = ttk.Combobox( width=70, textvariable=varforensic)
        cbforensics.bind("<Return>", cbinfo_onEnter)
        cbforensics.bind("<<ComboboxSelected>>", cbinfo_onEnter)
        cbforensics['values']=(forensiclist)
        cbforensics.place(relx=0.115, rely=0.42)

        #Web Application Drop Down
        cbweb = ttk.Combobox( width=70, textvariable=varwebapp)
        cbweb.bind("<Return>", cbinfo_onEnter)
        cbweb.bind("<<ComboboxSelected>>", cbinfo_onEnter)
        cbweb['values']=(webapplist)
        cbweb.place(relx=0.115, rely=0.48)

        #Stress Testing Drop Down
        cbstress = ttk.Combobox( width=70, textvariable=varstress)
        cbstress.bind("<Return>", cbinfo_onEnter)
        cbstress.bind("<<ComboboxSelected>>", cbinfo_onEnter)
        cbstress['values']=(stresslist)
        cbstress.place(relx=0.115, rely=0.54)

        #Sniffing & Spoofind Drop Down
        cbsniff = ttk.Combobox( width=70, textvariable=varsniff)
        cbsniff.bind("<Return>", cbinfo_onEnter)
        cbsniff.bind("<<ComboboxSelected>>", cbinfo_onEnter)
        cbsniff['values']=(snifflist)
        cbsniff.place(relx=0.115, rely=0.60)

        #Password Drop Down
        cbpass = ttk.Combobox( width=70, textvariable=varpass)
        cbpass.bind("<Return>", cbinfo_onEnter)
        cbpass.bind("<<ComboboxSelected>>", cbinfo_onEnter)
        cbpass['values']=(passlist)
        cbpass.place(relx=0.115, rely=0.66)

        #Hardware Hacking Drop Down
        cbhard = ttk.Combobox( width=70, textvariable=varhard)
        cbhard.bind("<Return>", cbinfo_onEnter)
        cbhard.bind("<<ComboboxSelected>>", cbinfo_onEnter)
        cbhard['values']=(hardlist)
        cbhard.place(relx=0.115, rely=0.72)

        #Reverse Engineering Drop Down
        cbreverse = ttk.Combobox( width=70, textvariable=varreverse)
        cbreverse.bind("<Return>", cbinfo_onEnter)
        cbreverse.bind("<<ComboboxSelected>>", cbinfo_onEnter)
        cbreverse['values']=(reverselist)
        cbreverse.place(relx=0.115, rely=0.78)

        #Reporting tools Drop Down
        cbreport = ttk.Combobox( width=70, textvariable=varreport)
        cbreport.bind("<Return>", cbinfo_onEnter)
        cbreport.bind("<<ComboboxSelected>>", cbinfo_onEnter)
        cbreport['values']=(reportlist)
        cbreport.place(relx=0.115, rely=0.84)

        #All tools Drop Down
        cball = ttk.Combobox( width=70, textvariable=varall)
        cball.bind("<Return>", cbinfo_onEnter)
        cball.bind("<<ComboboxSelected>>", cbinfo_onEnter)
        cball['values']=(alllist)
        cball.place(relx=0.115, rely=0.90)


    #A testing command
    def test(text):
        print 'In development phase.'+text

    def mydownloadf():
        mydownloads()

    def reportf():
        report()

    def search():
        search = Tk()
        search.geometry("336x93+518+273")
        search.title("Search")
        search.configure(background="#d9d9d9")
        search.wm_iconbitmap('images/icon.ico')
        search.resizable(0,0)

        SearchEntry = ttk.Entry(search)
        SearchEntry.place(relx=0.12, rely=0.32, relheight=0.23, relwidth=0.55)
        SearchEntry.configure(width=186)
        SearchEntry.configure(takefocus="")
        SearchEntry.configure(cursor="ibeam")

        def tobesearch():
            searchingtext = SearchEntry.get()
            search.destroy()

            def ok():
                searching.destroy()
                savedownloads(searchingtext)
                startdownload()

            def cancel():
                searching.destroy()

            def yes():
                searching.destroy()
                suggestions()

            #print searchingtext
            if searchingtext.lower() in alltools:
                searching = Tk()
                searching.geometry("322x155+456+155")
                searching.title("Search")
                searching.configure(background="#d9d9d9")
                #searching.wm_iconbitmap('images/icon.ico')
                searching.resizable(0,0)

                Searching = ttk.Label(searching)
                Searching.place(relx=0.33, rely=0.13, height=29, width=186)
                Searching.configure(background="#d9d9d9")
                Searching.configure(foreground="#000000")
                Searching.configure(relief=FLAT)
                Searching.configure(text='''Awesome! We found''')
                Searching.configure(width=186)

                Searching2 = ttk.Label(searching)
                Searching2.place(relx=0.4, rely=0.32, height=19, width=186)
                Searching2.configure(background="#d9d9d9")
                Searching2.configure(foreground="#000000")
                Searching2.configure(relief=FLAT)
                Searching2.configure(text=searchingtext)

                SearchingButtono = ttk.Button(searching, command=ok)
                SearchingButtono.place(relx=0.12, rely=0.65, height=25, width=76)
                SearchingButtono.configure(takefocus="")
                SearchingButtono.configure(text='''Continue''')

                SearchingButtonn = ttk.Button(searching, command=cancel)
                SearchingButtonn.place(relx=0.59, rely=0.65, height=25, width=76)
                SearchingButtonn.configure(takefocus="")
                SearchingButtonn.configure(text='''Cancel''')
            else:
                searching = Tk()
                searching.geometry("322x155+456+155")
                searching.title("Oops! Can't found any tool")
                searching.configure(background="#d9d9d9")
                searching.wm_iconbitmap('images/icon.ico')
                searching.resizable(0,0)

                Searching = ttk.Label(searching)
                Searching.place(relx=0.20, rely=0.13, height=29, width=186)
                Searching.configure(background="#d9d9d9")
                Searching.configure(foreground="#000000")
                Searching.configure(relief=FLAT)
                Searching.configure(text='''Wanna send us suggestion about''')
                Searching.configure(width=186)

                Searching2 = ttk.Label(searching)
                Searching2.place(relx=0.4, rely=0.32, height=19, width=186)
                Searching2.configure(background="#d9d9d9")
                Searching2.configure(foreground="#000000")
                Searching2.configure(relief=FLAT)
                Searching2.configure(text=searchingtext)

                SearchingButtono = ttk.Button(searching, command=yes)
                SearchingButtono.place(relx=0.12, rely=0.65, height=25, width=76)
                SearchingButtono.configure(takefocus="")
                SearchingButtono.configure(text='''Yes''')

                SearchingButtonn = ttk.Button(searching, command=cancel)
                SearchingButtonn.place(relx=0.59, rely=0.65, height=25, width=76)
                SearchingButtonn.configure(takefocus="")
                SearchingButtonn.configure(text='''No''')

        SearchButton = ttk.Button(search, command = tobesearch)
        SearchButton.place(relx=0.71, rely=0.32, height=25, width=76)
        SearchButton.configure(takefocus="")
        SearchButton.configure(text='''Search''')



    #Here is the top menubar
    menubar = Menu(root)

    homemenu = Menu(menubar, tearoff=0)
    homemenu.add_command(label="Download Section", command=downloadsection)
    homemenu.add_command(label="My Downloads", command=mydownloadf)
    homemenu.add_separator()
    homemenu.add_command(label="About me", command=aboutme)
    homemenu.add_separator()
    homemenu.add_command(label="Contact", command=contact)
    menubar.add_cascade(label = "Home", menu=homemenu)

    aboutmenu = Menu(menubar, tearoff=0)
    aboutmenu.add_command(label="About this Tool", command=about)
    aboutmenu.add_command(label="Licenses", command=licenses)
    aboutmenu.add_separator()
    aboutmenu.add_command(label="Check for Updates", command=checkupdates)
    aboutmenu.add_separator()
    aboutmenu.add_command(label="Contributors", command=contributions)
    aboutmenu.add_command(label="Send me suggestions", command=suggestions)
    aboutmenu.add_command(label="Report a tool", command=reportf)
    menubar.add_cascade(label="About", menu=aboutmenu)

    menubar.add_command(label="Search",command=search)

    menubar.add_command(label = "Quit", command = sys.exit)

    root.config(menu=menubar)

    #Here menu bar ends.

    #Here the programs starts
    downloadsection()

    root.mainloop()

atexit.register(atgexit)

if __name__ == '__main__':
    mainbody()
