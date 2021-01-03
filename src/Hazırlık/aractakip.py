import cv2
import numpy as np
import vehicles
import time

ykr_sayac=0
asagı_sayac=0


cap=cv2.VideoCapture("cars.mp4")

#videonun genişliği ayarlıyoruz
w=cap.get(3)
h=cap.get(4)
frameArea=h*w
areaTH=frameArea/400

#Çizgiler
yukarı_cizgi=int(2*(h/5))
asagı_cizgi=int(3*(h/5))

yukarı=int(1*(h/5))
asagı=int(4*(h/5))

pt5 =  [0, yukarı]
pt6 =  [w, yukarı]
pts_L3 = np.array([pt5,pt6], np.int32)
pts_L3 = pts_L3.reshape((-1,1,2))
pt7 =  [0, asagı]
pt8 =  [w, asagı]
pts_L4 = np.array([pt7,pt8], np.int32)
pts_L4 = pts_L4.reshape((-1,1,2))



kernalOp = np.ones((3,3),np.uint8)
kernalOp2 = np.ones((5,5),np.uint8)
kernalCl = np.ones((11,11),np.uint)


font = cv2.FONT_HERSHEY_SIMPLEX
araba = []
pid = 1

sub = cv2.createBackgroundSubtractorMOG2()  

ret, frame = cap.read()  
ratio = 1.0 

while(cap.isOpened()):


    ret, frame = cap.read()  
    if not ret: 
        frame = cv2.VideoCapture("cars.mp4")
        continue
    if ret: 
        image = cv2.resize(frame, (0, 0), None, ratio, ratio)  
        cv2.imshow("Ana Goruntu", image) 
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  
        cv2.imshow("Gray Goruntu", gray) 
        fgmask = sub.apply(gray)
        cv2.imshow("Hareket_algilama", fgmask) #hareket algılama 
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))  
        closing = cv2.morphologyEx(fgmask, cv2.MORPH_CLOSE, kernel)
        cv2.imshow("Bel_Nok_Giderme", closing) #belirlenen yerdeki noktaları gideriyor
        opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel)
        cv2.imshow("Cev_Nok_Giderme", opening) #çevredeki noktaları siliyor
        dilation = cv2.dilate(opening, kernel)
        cv2.imshow("Nesneleri kalinlastirma", dilation) #kalınlaştırıyor
        retvalbin, bins = cv2.threshold(dilation, 220, 255, cv2.THRESH_BINARY)  
        cv2.imshow("Binary", retvalbin) # nesne belirlemek için binary koda çeviriyor

        im2, contours, hierarchy = cv2.findContours(bins, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # aynı renk yoğunluğuna sahip bölgeleri birleştiriyor.
        

        #sekilleri buluyoruz
        _, countours,hierarchy=cv2.findContours(bins,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
        for cnt in countours:
            area=cv2.contourArea(cnt)
            print(area)
            if area>areaTH:
                
                #dikdörtgen için 
                m=cv2.moments(cnt)
                cx=int(m['m10']/m['m00'])
                cy=int(m['m01']/m['m00'])
                x,y,w,h=cv2.boundingRect(cnt)

                #dikdörtgeni çizdiriyoruz
                cv2.circle(frame,(cx,cy),5,(0,0,255),-1)
                img=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

                new=True
                if cy in range(yukarı,asagı):
                    for i in araba:
                        if abs(x - i.getX()) <= w and abs(y - i.getY()) <= h:
                            new = False
                            i.koordinat(cx, cy)

                            if i.yukari_giden(asagı_cizgi,yukarı_cizgi)==True:
                                ykr_sayac+=1
                                print("ID:",i.getId(),time.strftime("%c"))
                            
                            break
                    if new==True: #hiç bulunamazsa yeni
                        p=vehicles.Arac(pid,cx,cy)
                        araba.append(p)
                        pid+=1

        #Araç sayisini yazdırıyoruz
        str_yukarı='Arac Sayisi: '+str(ykr_sayac)
        
        #çizgileri çiziyorlar
        frame=cv2.polylines(frame,[pts_L3],False,(255,255,255),thickness=1)
        frame=cv2.polylines(frame,[pts_L4],False,(255,255,255),thickness=1)
        
        #yazının rengi ve kalınlığı
        cv2.putText(frame, str_yukarı, (10, 40), font, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(frame, str_yukarı, (10, 40), font, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
        
        cv2.imshow('Frame',frame)

        if cv2.waitKey(1)&0xff==ord('q'):
            break

    else:
        break

cap.release()
cv2.destroyAllWindows()

    







