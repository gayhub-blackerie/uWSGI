#coding=utf-8
import requests,sys
result_url=[]

def main():
    counts=open(sys.argv[1]).readlines()
    for line in open(sys.argv[1]):
        line=line.strip("\n")
        url=line
        try:
            #url="http://s6000.sgcc.com.cn/WebContent/s6000/main/index.jsp#no-back"
            r=requests.get(url,verify=True,timeout=3)
            print(url+" "+str(r.status_code))
            print(str(r.text))
            if r.status_code==200 and "MPEGVideo" in r.text:
                result_url.append(url)              
        except Exception as e:
            print(str(e))
    for i in result_url:
        print(i)
        file_200.write(i+"\n")

if __name__ == '__main__':
    file_200=open("result_uWSGI_file.txt","w")    
    main()
    file_200.flush()    
    file_200.close()   
