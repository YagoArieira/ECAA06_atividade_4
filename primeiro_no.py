import rospy
from std_msgs.msg import String

rospy.init_node('ativ4')
numero = 'matricula: 2017006077' #valor inicial para "numero"

def num_callBack(msg):
    global numero
    numero = msg.data #passar o valor de msg.data para "numero"

def timerCallBack(event):
    
    msg = String() 
    msg.data = '2017006077' #passar a matricula para msg.data
    pub.publish(msg) #publicar msg
    print(numero)

pub = rospy.Publisher('/matricula', String,queue_size=1) #publicar msg no topico /matricula

timer = rospy.Timer(rospy.Duration(1),timerCallBack)

sub = rospy.Subscriber('/soma',String,num_callBack) #passar a soma realizada no segundo_no.py para "numero"

rospy.spin()

