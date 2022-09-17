---
title: 'Unity 学习'
date: 2021-04-10 13:56:05
tags: [Unity]
published: true
hideInList: false
feature: 
isTop: false
---
```
常用生命周期
Awake() Start() Update() FixedUpdate()// 间隔每一帧的时间相同


 if (Input.GetKey(KeyCode.Space))
 {
    for (int i = 0; i < m_Weapons.Count; i++)
    {
        m_Weapons[i].TryAttack();
    }
}

//交互事件
GetButtonDown：true 
按下的第一帧为True下一帧之后都为false
GetButton:按下一直为true
GetButtonUp:抬起的第一帧为True ,下一帧之后为false

if (Input.GetAxis("Horizontal")!=0)
            {
                Debug.Log(Input.GetAxis("Horizontal"));
            }

            if (Input.GetAxis("Vertical") != 0)
            {
                Debug.Log(Input.GetAxis("Vertical"));
            }
            
Instantiate //克隆游戏对象  
//Instantiate(gameObject,position,rotation)    

//Invoke
Invoke("InvokeTest", 1);//一秒后执行
InvokeRepeating ("InvokeTest", 1,1);// 间隔一秒，之后一秒执行
CancelInvoke();//停止所有
CancelInvoke("InvokeTest");//暂停InvokeTest
        public void InvokeTest()
        {

        } 
        
          
//枚举
public  enum EntityType { W, N, S, D };
public EntityType _EntityType = EntityType.W;   
```