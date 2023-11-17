import os

print("ป้อนตัวเลขเพื่อเริ่มต้นการทำงาน \n1. สร้างไฟล์วิชาใหม่เพื่อเพิ่มข้อมูล \n2. เลือกวิชาและเพิ่มข้อมูลต่อท้ายไฟล์ \n3. เลือกวิชาและอ่านข้อมูลจากไฟล์มาแสดงผล \n4. เลือกวิชาและลบไฟล์ \n0. จบการทํางาน")

try:
    choose = input("กรุณาเลือกคำสั่งที่คุณต้องการใช้งาน: ")
    if choose not in ["0","1","2","3","4"] :
        print("กรุณาเลือกเมนู 1, 2, 3, 4 หรือ 0 เท่านั้น")

    if choose == "1" :
        subname = input("โปรดใส่ชื่อรายวิชาของคุณ (.txt): ")

        if ".txt" not in subname :
            print("ชื่อสกุลไฟล์ไม่ถูกต้อง กรุณาใส่หม่")

        else :
            name_sd = input("กรุณาป้อนชื้อ - นามสกุล: ")
            midscroe = int(input("กรุณาป้อนคะแนนกลางภาค: "))
            FNscore = int(input("กรุณาป้อนคะแนนปลายภาค: "))
            accuscore = int(input("กรุณาป้อนคะแนนก็บ: "))
            totalscore = midscroe + FNscore + accuscore
            
            if totalscore >= 50 :
                result = "ผ่าน"
                SJDetail = open(f"{subname}.txt", "w", encoding="utf-8")
                SJDetail.write(f"\nนักศึกษา {name_sd} \nคะแนนกลางภาค: {midscroe} \nคะแนนปลายภาค: {FNscore} \nคะแนนเก็บ: {accuscore} \nคะแนนรวม: {totalscore} \nผลลัพธ์ :{result} \n \n")
                print("สร้างไฟล์ใหม่และเพิ่มข้อมูลลงไฟล์เรียบร้อยแล้ว")
                SJDetail.close()

            else :
                result = "ไม่ผ่าน"
                SJDetail = open(f"{subname}.txt","w", encoding="ulf-8")
                SJDetail.write(f"\nนักศึกษา {name_sd} \nคะแนนกลางภาค: {midscroe} \nคะแนนปลายภาค: {FNscore} \nคะแนนเก็บ: {accuscore} \nคะแนนรวม: {totalscore} \nผลลัพธ์ :{result} \n \n")
                print("สร้างไฟล์ใหม่และเพิ่มข้อมูลลงไปไฟล์เรียบร้อยแล้ว")
                SJDetail.close()

    if choose == "2" :

        SJFileName = os.listdir()
        if not SJFileName :
            print("ไม่มีไฟล์ใด ๆ อยู่เลย")
            exit

        else :
            for i in SJFileName :
                print(i)
            fileSL = input("คุณต้องการเปิดไฟล์อะไร (พิมพ์ชื่อไฟล์ให้ถูกต้อง): ")

            if fileSL not in SJFileName :
                print("คุณพิมพ์ชื่อไฟล์ผิด")

            elif fileSL in SJFileName :
                SJMod = open(f"{fileSL}", "a+", encoding="ut-8")
                name_sd = input("กรุณาป้อนชื้อ - นามสกุล: ")
                midscroe = int(input("กรุณาป้อนคะแนนกลางภาค: "))
                FNscore = int(input("กรุณาป้อนคะแนนปลายภาค: "))
                accuscore = int(input("กรุณาป้อนคะแนนก็บ: "))
                totalscore = midscroe + FNscore + accuscore

                if totalscore >= 50 :
                    result = "ผ่าน"
                    SJMod.write(f"นักศึกษา {name_sd} \nคะแนนกลางภาค: {midscroe} \nคะแนนปลายภาค: {FNscore} \nคะแนนเก็บ: {accuscore} \nคะแนนรวม: {totalscore} \nผลลัพธ์ :{result} \n \n")
                    print("เพิ่มข้อมูลต่อท้ายไฟล์เรียบร้อยแล้ว")
                    SJMod.close()

                else : 
                    result = "ไม่ผ่าน"
                    SJMod.write(f"นักศึกษา {name_sd} \nคะแนนกลางภาค: {midscroe} \nคะแนนปลายภาค: {FNscore} \nคะแนนเก็บ: {accuscore} \nคะแนนรวม: {totalscore} \nผลลัพธ์ :{result} \n \n")
                    print("เพิ่มข้อมูลต่อท้ายไฟล์เรียบร้อยแล้ว")
                    SJMod.close()
    if choose == "3" :
        SJFileName = os.listdir()
        if not SJFileName :
            print("ไม่มีไฟล์ใดๆอยู่เลย")
            exit

        else :
            for i in SJFileName :
                if i.endswith(".txt"):
                    print(i)
            FChoose = input("คุณต้องการอ่านไฟล์อะไร (พิมพ์ชื่อไฟล์ให้ถูกต้อง): ")

            if FChoose not in SJFileName :
                print("คุณพิมพ์ชื่อไฟล์ผิด")

            elif FChoose in SJFileName :
                subjectRead = open(f"{FChoose}", "r", encoding="utf-8")
                reds = subjectRead.read()
                print(reds)
   
    if choose == "4" :
        SJFileName = os.listdir()
        if not SJFileName:
            print("ไม่มีไฟล์ใดๆอยู่เลย")
            exit

        else :
            for i in SJFileName :
                print(i)
            FChoose = input("คุณต้องการเปิดไฟล์อะไร (พิมพ์ชื่อไฟล์ให้ถูกต้อง): ")

            if FChoose not in SJFileName :
                print("คุณพิมพ์ชื่อไฟล์ผิด")

            elif FChoose in SJFileName :
                os.remove(f"{FChoose}")
                print("ลบไฟล์เรียบร้อย")

    if choose == "0" :
        exit
        
except Exception :
    print("เกิดข้อผิดพลาด กรุณากรอกเมนูตามตัวเลือก")