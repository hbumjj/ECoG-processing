#2W_ECoG
class ECoG_data:
    
    def __init__(self,name): 
        self.name=name
        
    def load_data(self): # 데이터 읽기 
        f=open(self.name,'r')
        lines=f.readlines()
        ecog_data,time_data,trigger_data=[],[],[]
        for i in lines: 
            time_data.append(float(i.split(" ")[3]))
            ecog_data.append(float(i.split(" ")[-4]))
            trigger_data.append(float(i.split(" ")[-1]))
        f.close()
        return time_data,ecog_data, trigger_data
    
    def Trigger_result(self): # 데이터 파싱
        result=[]
        time,ecog,trigger=ECoG_data.load_data(self)
        for number in range(1,9):
            sum_,trigger_number=[0]*2000,0
            for i in range(len(trigger)):
                if trigger[i] == float(number):
                    data= ecog[i-300:i+1700]
                    sum_=[sum_[i]+data[i] for i in range(len(sum_))]; trigger_number+=1
            result.append([sum_[i]/trigger_number for i in range(len(sum_))])
        return result
         
    def show_result(self): # 그래프로 확인
        import matplotlib.pyplot as plt
        import numpy as np
        time,ecog,trigger=ECoG_data.load_data(self)
        parsing_time=np.linspace(0,2,2000)
        plt.figure(figsize=(15,6))
        plt.subplot(2,1,1); plt.title('ECoG Data');plt.xlabel('time(s)'); plt.ylabel('ECoG(mv)'); plt.plot(time,ecog,linewidth=1)
        plt.subplot(2,1,2); plt.title('AEP Processing');plt.xlabel('time(s)'); plt.ylabel('averaged AEP(mv)') 
        result=ECoG_data.Trigger_result(self)
        label_name=['Ear','Eye','Neck','Nose','Three','Five','Nine','Ten']
        for i in range(len(result)):
            plt.plot(parsing_time,result[i],linewidth=1,label=label_name[i])
        plt.legend(loc=1); plt.tight_layout(); plt.show()
            
if __name__ == "__main__":
    ECoG_data('ECoG.txt').show_result() # 파일명 입력 
    
