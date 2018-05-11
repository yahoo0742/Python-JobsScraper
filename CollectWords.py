import collections
import lxml.html
import os
import re

def CollectGeneralText(htmlTxt):
    generalTxt = lxml.html.fromstring(htmlTxt).text_content()
    #print(generalTxt)
    return generalTxt

def GetBlacklist():
    cwd = os.getcwd()
    with open(cwd+'/blacklist.txt','r', encoding='utf-8') as f:
        text = f.read()
        #print(text)
        lst = text.split(',')
        return lst
    return None

Blacklist = []
HeadInvalidRE = r'^(^\.|[^A-Za-z]+)'
TailInvalidRE = r'[^\w#]+$'
HeadRex = re.compile(HeadInvalidRE)
TailRex = re.compile(TailInvalidRE)
    
def Collect(htmlTxt):
    global Blacklist
    if Blacklist == None or len(Blacklist) == 0:
        Blacklist = GetBlacklist()
        #print(Blacklist)
    text = CollectGeneralText(htmlTxt)
    resultList = text.split()
    resultList = [TailRex.sub('',HeadRex.sub('',x)) for x in resultList]
    resultList = [x for x in resultList if len(x) >= 1]
    collection = set(x for x in resultList if x not in Blacklist)#collections.Counter(x for x in resultList if x not in ignore)
    #print(collection)
    return collection

'''<div class="templatetext">
          <p> </p>
          <p> </p>
          <ul>
            <li>
              <div><strong>Specialist projects environment. </strong></div><strong>
</strong></li>
            <li><strong>Global &amp; Household Named Organisation 
</strong></li>
            <li><strong>$125,000 base per annum</strong></li>
          </ul>
          <p>We are urgently seeking at least x2  highly experienced ReactJS Full Stack Developers to join a project driven environment here in Auckland and one that specialises in SaaS, OpenSource and AWS Cloud based solutions. This is very much a
            household name organisation who pride themselves in staying at the pinnacle of technology stacks.</p>
          <p> </p>
          <p>This is an opportunity that will allow you a huge amount of exposure to one of NZ's highest spec organizations and the eternally growing Cloud sector. where you will have responsibility for the end to end development of Mobile Applications.</p>
          <ul>
            <li><strong>Development</strong> - a minimum of 8yrs commercial experience </li>
            <li><strong>React JS</strong> - 2yrs minimum experiewnce and experienced in the development of at least one end to end project (essential) </li>
            <li><strong>Javascript Frameworks (other)</strong>- expertise in NodeJS (preferred) or AngularJS </li>
            <li>Database - ideally MongoDB or NoSQL / MySQL </li>
            <li><strong>Platform</strong> - Linux (preferred is CentOS or Ubuntu / Debian) </li>
            <li><strong>Other</strong> - GIT (essential), Redux, Restful API, SOA, JavaScript / HTML5 / CSS / Agile (essential) </li>
            <li><strong>Communication </strong>- Very high level of verbal and written communication skills is required</li>
          </ul>
          <p> </p>
          <p> </p>
          <p>Please do not hesitate in forwarding your CV via this website in a MS Word format. We are very keen to commence the interview process ASAP. </p>
          <p> </p>
          <p>*** We CANNOT offer Visa nor Relocation sponsorship for this role. It is essential that you already hold a valid and legal right to work in NZ at the time of application.</p>
          <p><br />For further information please call Carl Robinson on 09 302 7024 or apply direct by clicking below.</p>
          <p> </p>
        </div>'''

