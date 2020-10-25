import rospy
from std_msgs.msg import String


rospy.init_node('ativ4_soma')

valor = '0'

def topic_callBack(somaTot):
    global valor
    valor = somaTot.data #valor = 2017006077
    
rospy.Subscriber('/matricula',String, topic_callBack)

def timerCallBack(event): #realizar o calculo
    
    somaTot = 0
    
    
    for i in valor:
        somaTot = somaTot + int(i)

    msg = String()
    msg.data = str(somaTot)
    pub.publish(msg)

#2017006077 -> 2 + 0 + 1 + 7 + 0 + 0 + 6 + 0 + 7 + 7 = 30

pub = rospy.Publisher('/soma', String,queue_size=1) #publicar no segundo topico /soma
timer = rospy.Timer(rospy.Duration(0.1),timerCallBack)

rospy.spin()