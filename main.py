from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen
from kivy.uix.label import Label
from kivy.lang import Builder
from kivymd.uix.button import MDFillRoundFlatButton, MDRaisedButton, MDRectangleFlatButton,MDRoundFlatButton
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.layout import Layout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.scrollview import ScrollView
from kivymd.uix.list import ImageLeftWidget
from kivymd.uix.list import OneLineListItem, OneLineAvatarListItem
from kivy.core.audio import SoundLoader
# from jnius import autoclass
# from plyer import android


from kivy.graphics import Color, Rectangle

from kivy.uix.button import Button
import kivy

kivy.require('1.9.0')

from kivy.config import Config

Config.set('graphics', 'width', '200')
Config.set('graphics', 'height', '200')
from kivy.core.window import Window

Window.size = (350, 600)

screen_helper = ("""
#:import FadeTransition kivy.uix.screenmanager.FadeTransition
ScreenManager:
    Quote:
    Q1:
    Q2:
    Q3:
    Q4:
    Q5:
    Q6:
    Q7:
    GetSupport:
    Welcome:
    Disclaimer:
    Module:
    LearnList:
    Progress:
    SymptomsList:
    Q:
    Que1: 
    Grounding:
    DeepBreath:
    Que1_Example:
    Distress_meterUnableToSleep:
    Distress_meterWorried:
    Distress_meterSAD:
    Distress_meterDifficulty:
    Distress_meterAvoiding:
    Distress_meterReminded:
    Distress_meterAngry:
    LearnList:
    Soothing:
    Connect:
    Inspiring:
    PlayMusicScreen:
    MuscleRelax:
    CrisisResources:
    

 
    
<PlayMusicScreen>:
    name: 'play_music_screen'
    
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'
        MDTopAppBar:
            title: "[i]AmbietSound[/i]"
            specific_text_color: "white"
            elevation: 2
            anchor_title: "center"
            left_action_items: [["home", lambda x: root.manager.set_screen('module')]]
            markup:True
    
    ScrollView:
        
        
        MDList:
            pos_hint:{"center_x":0.5,"center_y":0.7}
            padding:[40,0]
            
            OneLineAvatarListItem:
                text:"Flute"
                source:"flute.png"
                on_release: root.flute()
                
                
            OneLineAvatarListItem:
                text:"Birds"
                source:"bird.png"
                on_release: root.birds()
            OneLineAvatarListItem:
                text:"Stream"
                source:""
                on_release: root.stream()
            OneLineAvatarListItem:
                text:"Waterfall"
                source:"waterfall.png"
                on_release: root.waterfall()
    MDFillRoundFlatButton:
        text:"Home"
        on_release:root.manager.current='module'
        
<Q4>:
    name: "q4"
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'
        MDTopAppBar:
            title: "[i]How common is PTSD?[/i]"
            specific_text_color: "white"
            elevation: 2
            anchor_title: "center"
    BoxLayout:
        orientation:"vertical"
        spacing: "50dp"
        padding: "20dp"
        adaptive_height: True
        background_color:'Teal'
        pos_hint:{'center_x':0.5,'center_y':0.4}
        size_hint:(0.7,0.7)
    Image:
        source: "commonptsd.png"
        size_hint: 0.9, 0.9
        pos_hint: {"center_x": 0.5, "center_y": 0.7}
    MDFillRoundFlatButton:
        text:"Home"
        on_release:root.manager.current='module' 
    MDLabel:
        text:"Although most people feel much better within a month or two after a trauma, some people develop PTSD or other problems like depression or substance use problems."
        pos_hint: {"center_x": 0.5, "center_y": 0.45}
        halign: "left"
        font_size: "13sp"
        padding:[20,0]
    MDLabel:
        text:"Did you know?"
        pos_hint: {"center_x": 0.5, "center_y": 0.36}
        halign: "left"
        font_size: "14sp"
        true:"Bold"
        padding:[20,0]
    MDFillRoundFlatButton:
        text:"Home"
        on_release:root.manager.current='module'
    MDLabel:
        text:"* About 7% of the US population will have PTSD in their lifetime."
        pos_hint: {"center_x": 0.5, "center_y": 0.30}
        halign: "left"
        font_size: "13sp"
        padding:[20,0]
    MDLabel:
        text:"* Certain types of trauma, such as rape and combat, can cause even higher rates of PTSD."
        pos_hint: {"center_x": 0.5, "center_y": 0.20}
        halign: "left"
        font_size: "13sp"
        padding:[20,0]
<Grounding>:
    name: "grounding"
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'
        MDTopAppBar:
            title: "[i]Grounding[/i]"
            specific_text_color: "white"
            elevation: 2
            anchor_title: "center"
    BoxLayout:
        orientation:"vertical"
        spacing: "50dp"
        padding: "20dp"
        adaptive_height: True
        background_color:'Teal'
        pos_hint:{'center_x':0.5,'center_y':0.4}
        size_hint:(0.7,0.7)
    Image:
        source: "grounding.png"
        size_hint: 0.9, 0.5
        pos_hint: {"center_x": 0.5, "center_y": 0.6}
    MDFillRoundFlatButton:
        text:"Home"
        on_release:root.manager.current='module'  
    MDLabel:
        text:"Focus all of your attention on your feet. Feel the floor under them. Focus all of your attention on the feel of floor. Focus your attention on the smells in your environment. Focus on and listen carefully to all the sounds in your environment while keeping your eyes close."
        pos_hint: {"center_x": 0.5, "center_y": 0.2}
        halign: "left"
        font_size: "13sp"
        padding:[20,0]   
<DeepBreath>:
    name: "deepbreath"
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'
        MDTopAppBar:
            title: "[i]Deep Breathing[/i]"
            specific_text_color: "white"
            elevation: 2
            anchor_title: "center"
    BoxLayout:
        orientation:"vertical"
        spacing: "50dp"
        padding: "20dp"
        adaptive_height: True
        background_color:'Teal'
        pos_hint:{'center_x':0.5,'center_y':0.4}
        size_hint:(0.7,0.7)
    MDFillRoundFlatButton:
        text:"Home"
        on_release:root.manager.current='module' 
    Image:
        source: "newM.png"
        size_hint: 0.9, 0.5
        pos_hint: {"center_x": 0.5, "center_y": 0.6}
    MDLabel:
        text:"Slowing down and deepening your breathing can help you calm down when you feel distress. Put on your headphones or go somewhere private and quiet to be led through the exercise."
        pos_hint: {"center_x": 0.5, "center_y": 0.3}
        halign: "left"
        font_size: "13sp"
        padding:[20,0]
<Q5>:
    name: "q5"
    ScrollView:
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'
        MDTopAppBar:
            title: "[i]Who develops PTSD?[/i]"
            specific_text_color: "white"
            elevation: 2
            anchor_title: "center"
    BoxLayout:
        orientation:"vertical"
        spacing: "50dp"
        padding: "20dp"
        adaptive_height: True
        background_color:'Teal'
        pos_hint:{'center_x':0.5,'center_y':0.4}
        size_hint:(0.7,0.7)
    Image:
        source: "developptsd.png"
        size_hint: 0.9, 0.9
        pos_hint: {"center_x": 0.5, "center_y": 0.7}
    MDFillRoundFlatButton:
        text:"Home"
        on_release:root.manager.current='module' 
    MDLabel:
        text:"Virtually anyone can develop PTSD. However, there are some factors that make it more likely."
        pos_hint: {"center_x": 0.5, "center_y": 0.55}
        halign: "left"
        font_size: "13sp"
        padding:[20,0]
    MDLabel:
        text:"Risk factors before a trauma:"
        pos_hint: {"center_x": 0.5, "center_y": 0.50}
        halign: "left"
        font_size: "14sp"
        true:"Bold"
        padding:[20,0]
    MDLabel:
        text:"* having been abused as a child "
        pos_hint: {"center_x": 0.6, "center_y": 0.46}
        halign: "left"
        font_size: "13sp"
        padding:[20,0]
    MDLabel:
        text:"* having a pre-existing mental health problem"
        pos_hint: {"center_x": 0.6, "center_y": 0.42}
        halign: "left"
        font_size: "13sp"
        padding:[20,0]
    MDLabel:
        text:"* having a family history of mental illness "
        pos_hint: {"center_x": 0.6, "center_y": 0.38}
        halign: "left"
        font_size: "13sp"
        padding:[20,0]
    MDLabel:
        text:" Risk factors during a trauma:"
        pos_hint: {"center_x": 0.5, "center_y": 0.33}
        halign: "left"
        font_size: "14sp"
        padding:[20,0]
    MDLabel:
        text:"* believing you will die"
        pos_hint: {"center_x": 0.6, "center_y": 0.29}
        halign: "left"
        font_size: "13sp"
        padding:[20,0]
    MDLabel:
        text:"*feeling completely helpless"
        pos_hint: {"center_x": 0.6, "center_y":0.25}
        halign: "left"
        font_size: "13sp"
        padding:[20,0]
    MDLabel:
        text:"*being seriously injured"
        pos_hint: {"center_x": 0.6, "center_y":0.21}
        halign: "left"
        font_size: "13sp"
        padding:[20,0]
    MDLabel:
        text:" Risk factors during a trauma:"
        pos_hint: {"center_x": 0.5, "center_y": 0.17}
        halign: "left"
        font_size: "14sp"
        padding:[20,0]
    MDLabel:
        text:"*lack of social support"
        pos_hint: {"center_x": 0.6, "center_y":0.13}
        halign: "left"
        font_size: "13sp"
        padding:[20,0]
    MDLabel:
        text:"*additional life stresses (such as job loss, divorce)"
        pos_hint: {"center_x": 0.6, "center_y":0.10}
        halign: "left"
        font_size: "13sp"
        padding:[20,0]
    MDFillRoundFlatButton:
        text:"Home"
        on_release:root.manager.current='module'
<Q7>:
    name: "q7"
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'
        MDTopAppBar:
            title: "[i]Problem related to PTSD?[/i]"
            specific_text_color: "white"
            elevation: 2
            anchor_title: "center"
    BoxLayout:
        orientation:"vertical"
        spacing: "50dp"
        padding: "20dp"
        adaptive_height: True
        background_color:'Teal'
        pos_hint:{'center_x':0.5,'center_y':0.4}
        size_hint:(0.7,0.7)
    Image:
        source: "prblemPTSD.png"
        size_hint: 0.9, 0.9
        pos_hint: {"center_x": 0.5, "center_y": 0.7}
    MDFillRoundFlatButton:
        text:"Home"
        on_release:root.manager.current='module' 
    MDLabel:
        text:"Some other problems are more common for people with PTSD. These include:"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        halign: "left"
        font_size: "13sp"
        padding:[20,0]
    MDLabel:
        text:"* depression"
        pos_hint: {"center_x": 0.6, "center_y": 0.45}
        halign: "left"
        font_size: "13sp"
        padding:[20,0]
    MDLabel:
        text:"* alcohol and substance use problems"
        pos_hint: {"center_x": 0.6, "center_y": 0.40}
        halign: "left"
        font_size: "13sp"
        padding:[20,0]
    MDLabel:
        text:"* problems in relationships, work, school, or other important activities"
        pos_hint: {"center_x": 0.6, "center_y": 0.34}
        halign: "left"
        font_size: "13sp"
        padding:[20,0]
    MDLabel:
        text:"* physical symptoms (pain, headaches, digestive problems)"
        pos_hint: {"center_x": 0.6, "center_y": 0.28}
        halign: "left"
        font_size: "13sp"
        padding:[20,0]
    MDLabel:
        text:"* increased risk of medical problems"
        pos_hint: {"center_x": 0.6, "center_y": 0.24}
        halign: "left"
        font_size: "13sp"
        padding:[20,0]
    MDLabel:
        text:"Did you know?:"
        pos_hint: {"center_x": 0.5, "center_y": 0.20}
        halign: "left"
        font_size: "15sp"
        true:"Bold"
        padding:[20,0]
    MDLabel:
        text:"* More than half of men with PTSD have alcohol problems."
        pos_hint: {"center_x": 0.6, "center_y": 0.15}
        halign: "left"
        font_size: "13sp"
        padding:[20,0]
    MDLabel:
        text:"* Nearly half of women with PTSD have depression."
        pos_hint: {"center_x": 0.6, "center_y": 0.10}
        halign: "left"
        font_size: "13sp"
        padding:[20,0]
    MDFillRoundFlatButton:
        text:"Home"
        on_release:root.manager.current='module'
<Q6>:
    name: "q6"
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'
        MDTopAppBar:
            title: "[i]How long does PTSD last?[/i]"
            specific_text_color: "white"
            elevation: 2
            anchor_title: "center"
    BoxLayout:
        orientation:"vertical"
        spacing: "50dp"
        padding: "20dp"
        adaptive_height: True
        background_color:'Teal'
        pos_hint:{'center_x':0.5,'center_y':0.4}
        size_hint:(0.7,0.7)
    Image:
        source: "ptsdLast.png"
        size_hint: 0.9, 0.9
        pos_hint: {"center_x": 0.5, "center_y": 0.7}
    MDFillRoundFlatButton:
        text:"Home"
        on_release:root.manager.current='module' 
    MDLabel:
        text:"PTSD symptoms usually appear soon after a traumatic experience, however, in some cases symptoms do not appear for months or even years after the trauma. For some people who experience symptoms early, these symptoms go away on their own. For others, these symptoms can last for many years, especially if they do not seek help."
        pos_hint: {"center_x": 0.5, "center_y": 0.45}
        halign: "left"
        font_size: "13sp"
        padding:[20,0]
    MDLabel:
        text:"PTSD symptoms can worsen during times of stress or when people are reminded of what happened by trauma triggers (such as anniversaries of trauma). How long PTSD lasts also depends on whether effective treatment is received."
        pos_hint: {"center_x": 0.5, "center_y": 0.25}
        halign: "left"
        font_size: "13sp"
        padding:[20,0]
    MDFillRoundFlatButton:
        text:"Home"
        on_release:root.manager.current='module'
<Q3>:
    name: "q3"
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'
        MDTopAppBar:
            title: "[i]How does PTSD develop?[/i]"
            specific_text_color: "white"
            elevation: 2
            anchor_title: "center"
    BoxLayout:
        orientation:"vertical"
        spacing: "50dp"
        padding: "20dp"
        adaptive_height: True
        background_color:'Teal'
        pos_hint:{'center_x':0.5,'center_y':0.4}
        size_hint:(0.7,0.7)
    Image:
        source: "ptsdDevelop.png"
        size_hint: 0.9, 0.9
        pos_hint: {"center_x": 0.5, "center_y": 0.6}
    MDFillRoundFlatButton:
        text:"Home"
        on_release:root.manager.current='module' 
    MDLabel:
        text:"After trauma, it's normal to be in shock, have painful memories, and be upset by reminders. Trauma can also change how people think about themselves, others, and the world to more extreme ideas like  'nowhere is safe, 'or' no one can be trusted'."
        pos_hint: {"center_x": 0.5, "center_y": 0.45}
        halign: "left"
        font_size: "13sp"
        padding:[20,0]
    MDLabel:
        text:"For most, these reactions will lessen over time. But for some, these reactions continue and can be severe enough to disturb everyday life."
        pos_hint: {"center_x": 0.5, "center_y": 0.30}
        halign: "left"
        font_size: "13sp"
        padding:[20,0]   
    MDFillRoundFlatButton:
        text:"Home"
        on_release:root.manager.current='module' 
<Distress_meterWorried>:

    name:'distress_meterW'
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'
        # orientation:'vertical'
        MDTopAppBar:
            title: "[i]Distress  Meter[/i]"
            
            specific_text_color: "white"
            elevation: 2
            anchor_title: "center"
    MDLabel:
        text:"[i][b]What's your current level of distress?[/b][/i]"
        pos_hint: {"center_x":0.5, "center_y":0.8 }
        halign:'center'
        markup:True
        theme_text_color:'Custom'
        text_color:(0/ 255.0, 128/ 255.0, 128 / 255.0, 1)
        font_style:'Subtitle1'
    MDLabel:
        text: '[i]Select you level of distress.[/i]' 
        pos_hint: {"center_x": 0.5,"center_y":0.7 }
        halign:'center'
        markup:True
        theme_text_color:'Custom'
        text_color:(0/ 255.0, 128/ 255.0, 128 / 255.0, 1)
        font_style:'Subtitle1'
    MDFillRoundFlatButton:
        text:'1'
        on_release:root.manager.current='inspiring'
        pos:100,100
        font_size: 20
        # padding:[40,0]
        markup:True
        # theme_text_color:'Custom'tyoe
        # text_color:(0/ 255.0, 128/ 255.0, 128 / 255.0, 1)
        font_style:'Subtitle1'
        on_release:root.manager.current='musclerelax'
        
    
    MDFillRoundFlatButton:
        text:'3'
        # size_hint: 0.5,0.5
        pos:100,200
        font_size: 20
        # padding:[40,0]
        markup:True
        # theme_text_color:'Custom'tyoe
        # text_color:(0/ 255.0, 128/ 255.0, 128 / 255.0, 1)
        font_style:'Subtitle1'
        on_release:root.manager.current='soothing'
        
    
    MDFillRoundFlatButton:
        text:'5'
        # size_hint: 1,0.10
        pos:100,300
        font_size: 20
        # padding:[40,0]
        markup:True
        # theme_text_color:'Custom'
        # text_color:(0/ 255.0, 128/ 255.0, 128 / 255.0, 1)
        font_style:'Subtitle1'
        on_release:root.manager.current='grounding'
    MDFillRoundFlatButton:
        text:"Home"
        on_release:root.manager.current='module'
<Distress_meterSAD>:

    name:'distress_meterS'
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'
        # orientation:'vertical'
        MDTopAppBar:
            title: "[i]Distress  Meter[/i]"
            
            specific_text_color: "white"
            elevation: 2
            anchor_title: "center"
    MDLabel:
        text:"[i][b]What's your current level of distress?[/b][/i]"
        pos_hint: {"center_x":0.5, "center_y":0.8 }
        halign:'center'
        markup:True
        theme_text_color:'Custom'
        text_color:(0/ 255.0, 128/ 255.0, 128 / 255.0, 1)
        font_style:'Subtitle1'
        
    MDLabel:
        text: '[i]Select you level of distress.[/i]' 
        pos_hint: {"center_x": 0.5,"center_y":0.7 }
        halign:'center'
        markup:True
        theme_text_color:'Custom'
        text_color:(0/ 255.0, 128/ 255.0, 128 / 255.0, 1)
        font_style:'Subtitle1'
    MDFillRoundFlatButton:
        text:'1'
        
        pos:100,100
        font_size: 20
        # padding:[40,0]
        markup:True
        # theme_text_color:'Custom'tyoe
        # text_color:(0/ 255.0, 128/ 255.0, 128 / 255.0, 1)
        font_style:'Subtitle1'
        on_release:root.manager.current='connect'
        
    
    MDFillRoundFlatButton:
        text:'3'
        # size_hint: 0.5,0.5
        pos:100,200
        font_size: 20
        # padding:[40,0]
        markup:True
        # theme_text_color:'Custom'tyoe
        # text_color:(0/ 255.0, 128/ 255.0, 128 / 255.0, 1)
        font_style:'Subtitle1'
        on_release:root.manager.current='deepbreath'
    
    MDFillRoundFlatButton:
        text:'5'
        # size_hint: 1,0.10
        pos:100,300
        font_size: 20
        # padding:[40,0]
        markup:True
        # theme_text_color:'Custom'
        # text_color:(0/ 255.0, 128/ 255.0, 128 / 255.0, 1)
        font_style:'Subtitle1'
        # on_release:root.manager.current='screen_ques'
        on_release:root.manager.current='play_music_screen'
    MDFillRoundFlatButton:
        text:"Home"
        on_release:root.manager.current='module'
<Distress_meterDifficulty>:

    name:'distress_meterD'
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'
        # orientation:'vertical'
        MDTopAppBar:
            title: "[i]Distress  Meter[/i]"
            
            specific_text_color: "white"
            elevation: 2
            anchor_title: "center"
    MDLabel:
        text:"[i][b]What's your current level of distress?[/b][/i]"
        pos_hint: {"center_x":0.5, "center_y":0.8 }
        halign:'center'
        markup:True
        theme_text_color:'Custom'
        text_color:(0/ 255.0, 128/ 255.0, 128 / 255.0, 1)
        font_style:'Subtitle1'
    MDLabel:
        text: '[i]Select you level of distress.[/i]' 
        pos_hint: {"center_x": 0.5,"center_y":0.7 }
        halign:'center'
        markup:True
        theme_text_color:'Custom'
        text_color:(0/ 255.0, 128/ 255.0, 128 / 255.0, 1)
        font_style:'Subtitle1'
    MDFillRoundFlatButton:
        text:"Home"
        on_release:root.manager.current='module'
    MDFillRoundFlatButton:
        text:'1'
        
        pos:100,100
        font_size: 20
        # padding:[40,0]
        markup:True
        # theme_text_color:'Custom'tyoe
        # text_color:(0/ 255.0, 128/ 255.0, 128 / 255.0, 1)
        font_style:'Subtitle1'
        on_release:root.manager.current='soothing'
        
    
    MDFillRoundFlatButton:
        text:'3'
        # size_hint: 0.5,0.5
        pos:100,200
        font_size: 20
        # padding:[40,0]
        markup:True
        # theme_text_color:'Custom'tyoe
        # text_color:(0/ 255.0, 128/ 255.0, 128 / 255.0, 1)
        font_style:'Subtitle1'
        on_release:root.manager.current='play_music_screen'
        
    
    MDFillRoundFlatButton:
        text:'5'
        # size_hint: 1,0.10
        pos:100,300
        font_size: 20
        # padding:[40,0]
        markup:True
        # theme_text_color:'Custom'
        # text_color:(0/ 255.0, 128/ 255.0, 128 / 255.0, 1)
        font_style:'Subtitle1'
        on_release:root.manager.current='connect'
    MDFillRoundFlatButton:
        text:"Home"
        on_release:root.manager.current='module'
<Distress_meterAvoiding>:

    name:'distress_meterA'
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'
        # orientation:'vertical'
        MDTopAppBar:
            title: "[i]Distress  Meter[/i]"
            
            specific_text_color: "white"
            elevation: 2
            anchor_title: "center"
    MDLabel:
        text:"[i][b]What's your current level of distress?[/b][/i]"
        pos_hint: {"center_x":0.5, "center_y":0.8 }
        halign:'center'
        markup:True
        theme_text_color:'Custom'
        text_color:(0/ 255.0, 128/ 255.0, 128 / 255.0, 1)
        font_style:'Subtitle1'
    MDFillRoundFlatButton:
        text:"Home"
        on_release:root.manager.current='module'
    MDLabel:
        text: '[i]Select you level of distress.[/i]' 
        pos_hint: {"center_x": 0.5,"center_y":0.7 }
        halign:'center'
        markup:True
        theme_text_color:'Custom'
        text_color:(0/ 255.0, 128/ 255.0, 128 / 255.0, 1)
        font_style:'Subtitle1'
    MDFillRoundFlatButton:
        text:'1'
        
        pos:100,100
        font_size: 20
        # padding:[40,0]
        markup:True
        # theme_text_color:'Custom'tyoe
        # text_color:(0/ 255.0, 128/ 255.0, 128 / 255.0, 1)
        font_style:'Subtitle1'
        on_release:root.manager.current='soothing'
        
    
    MDFillRoundFlatButton:
        text:'3'
        # size_hint: 0.5,0.5
        pos:100,200
        font_size: 20
        # padding:[40,0]
        markup:True
        # theme_text_color:'Custom'tyoe
        # text_color:(0/ 255.0, 128/ 255.0, 128 / 255.0, 1)
        font_style:'Subtitle1'
        on_release:root.manager.current='grounding'
    
    MDFillRoundFlatButton:
        text:'5'
        # size_hint: 1,0.10
        pos:100,300
        font_size: 20
        # padding:[40,0]
        markup:True
        # theme_text_color:'Custom'
        # text_color:(0/ 255.0, 128/ 255.0, 128 / 255.0, 1)
        font_style:'Subtitle1'
        on_release:root.manager.current='connect'
    MDFillRoundFlatButton:
        text:"Home"
        on_release:root.manager.current='module'
<Distress_meterReminded>:

    name:'distress_meterRT'
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'
        # orientation:'vertical'
        MDTopAppBar:
            title: "[i]Distress  Meter[/i]"
            
            specific_text_color: "white"
            elevation: 2
            anchor_title: "center"
    MDLabel:
        text:"[i][b]What's your current level of distress?[/b][/i]"
        pos_hint: {"center_x":0.5, "center_y":0.8 }
        halign:'center'
        markup:True
        theme_text_color:'Custom'
        text_color:(0/ 255.0, 128/ 255.0, 128 / 255.0, 1)
        font_style:'Subtitle1'
    MDFillRoundFlatButton:
        text:"Home"
        on_release:root.manager.current='module'
    MDLabel:
        text: '[i]Select you level of distress.[/i]' 
        pos_hint: {"center_x": 0.5,"center_y":0.7 }
        halign:'center'
        markup:True
        theme_text_color:'Custom'
        text_color:(0/ 255.0, 128/ 255.0, 128 / 255.0, 1)
        font_style:'Subtitle1'
    MDFillRoundFlatButton:
        text:'1'
        
        pos:100,100
        font_size: 20
        # padding:[40,0]
        markup:True
        # theme_text_color:'Custom'tyoe
        # text_color:(0/ 255.0, 128/ 255.0, 128 / 255.0, 1)
        font_style:'Subtitle1'
        on_release:root.manager.current='soothing'
        
    
    MDFillRoundFlatButton:
        text:'3'
        # size_hint: 0.5,0.5
        pos:100,200
        font_size: 20
        # padding:[40,0]
        markup:True
        # theme_text_color:'Custom'tyoe
        # text_color:(0/ 255.0, 128/ 255.0, 128 / 255.0, 1)
        font_style:'Subtitle1'
        on_release:root.manager.current='inspiring'
    
    MDFillRoundFlatButton:
        text:'5'
        # size_hint: 1,0.10
        pos:100,300
        font_size: 20
        # padding:[40,0]
        markup:True
        # theme_text_color:'Custom'
        # text_color:(0/ 255.0, 128/ 255.0, 128 / 255.0, 1)
        font_style:'Subtitle1'
        on_release:root.manager.current='connect'
<Distress_meterAngry>:

    name:'distress_meterangre'
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'
        # orientation:'vertical'
        MDTopAppBar:
            title: "[i]Distress  Meter[/i]"
            
            specific_text_color: "white"
            elevation: 2
            anchor_title: "center"
    MDFillRoundFlatButton:
        text:"Home"
        on_release:root.manager.current='module'
    MDLabel:
        text:"[i][b]What's your current level of distress?[/b][/i]"
        pos_hint: {"center_x":0.5, "center_y":0.8 }
        halign:'center'
        markup:True
        theme_text_color:'Custom'
        text_color:(0/ 255.0, 128/ 255.0, 128 / 255.0, 1)
        font_style:'Subtitle1'
    MDLabel:
        text: '[i]Select you level of distress.[/i]' 
        pos_hint: {"center_x": 0.5,"center_y":0.7 }
        halign:'center'
        markup:True
        theme_text_color:'Custom'
        text_color:(0/ 255.0, 128/ 255.0, 128 / 255.0, 1)
        font_style:'Subtitle1'
    MDFillRoundFlatButton:
        text:'1'
        
        pos:100,100
        font_size: 20
        # padding:[40,0]
        markup:True
        # theme_text_color:'Custom'tyoe
        # text_color:(0/ 255.0, 128/ 255.0, 128 / 255.0, 1)
        font_style:'Subtitle1'
        on_release:root.manager.current='soothing'
    
    MDFillRoundFlatButton:
        text:'3'
        # size_hint: 0.5,0.5
        pos:100,200
        font_size: 20
        # padding:[40,0]
        markup:True
        # theme_text_color:'Custom'tyoe
        # text_color:(0/ 255.0, 128/ 255.0, 128 / 255.0, 1)
        font_style:'Subtitle1'
        on_release:root.manager.current='play_music_screen'
    
    MDFillRoundFlatButton:
        text:'5'
        # size_hint: 1,0.10
        pos:100,300
        font_size: 20
        # padding:[40,0]
        markup:True
        # theme_text_color:'Custom'
        # text_color:(0/ 255.0, 128/ 255.0, 128 / 255.0, 1)
        font_style:'Subtitle1'
        on_release:root.manager.current='musclerelax'
    MDFillRoundFlatButton:
        text:"Home"
        on_release:root.manager.current='module'
    
<Distress_meterUnableToSleep>:
    name:'distress_meterUTS'
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'
        # orientation:'vertical'
        MDTopAppBar:
            title: "[i]Distress  Meter[/i]"
            
            specific_text_color: "white"
            elevation: 2
            anchor_title: "center"
    MDFillRoundFlatButton:
        text:"Home"
        on_release:root.manager.current='module'
    MDLabel:
        text:"[i][b]What's your current level of distress?[/b][/i]"
        pos_hint: {"center_x":0.5, "center_y":0.8 }
        halign:'center'
        markup:True
        theme_text_color:'Custom'
        text_color:(0/ 255.0, 128/ 255.0, 128 / 255.0, 1)
        font_style:'Subtitle1'
    MDLabel:
        text: '[i]Select you level of distress.[/i]' 
        pos_hint: {"center_x": 0.5,"center_y":0.7 }
        halign:'center'
        markup:True
        theme_text_color:'Custom'
        text_color:(0/ 255.0, 128/ 255.0, 128 / 255.0, 1)
        font_style:'Subtitle1'
    MDFillRoundFlatButton:
        text:'1'
        
        pos:100,100
        font_size: 20
        # padding:[40,0]
        markup:True
        # theme_text_color:'Custom'tyoe
        # text_color:(0/ 255.0, 128/ 255.0, 128 / 255.0, 1)
        font_style:'Subtitle1'
        on_release:root.manager.current='inspiring'
    
    MDFillRoundFlatButton:
        text:'3'
        # size_hint: 0.5,0.5
        pos:100,200
        font_size: 20
        # padding:[40,0]
        markup:True
        # theme_text_color:'Custom'tyoe
        # text_color:(0/ 255.0, 128/ 255.0, 128 / 255.0, 1)
        font_style:'Subtitle1'
        on_release:root.manager.current='connect'
    
    MDFillRoundFlatButton:
        text:'5'
        # size_hint: 1,0.10
        pos:100,300
        font_size: 20
        # padding:[40,0]
        markup:True
        # theme_text_color:'Custom'
        # text_color:(0/ 255.0, 128/ 255.0, 128 / 255.0, 1)
        font_style:'Subtitle1'
        on_release:root.manager.current='play_music_screen'
    
    
<Quote>:
    name:'Chitta'
    MDLabel:
        text: '[i]It is during the darkest moments that we must focus to seen Light ! [/i]' 
        halign:'center'
        markup:True
        theme_text_color:'Custom'
        text_color:(0/ 255.0, 128/ 255.0, 128 / 255.0, 1)
        font_style:'Subtitle1'
        
    MDFillRoundFlatButton:
        text:"Get Started"
        pos_hint:{'center_x': 0.5, 'center_y': 0.3}
        on_release:root.manager.current='Welcome'
        
    Image:
        source:"icon.png"
        pos_hint:{"center_x":0.5,"center_y":0.7}
        size_hint:(0.5,0.3)
<Q1>:
    name: "q1"
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'
        MDTopAppBar:
            title: "[i]What is ptsd?[/i]"
            specific_text_color: "white"
            elevation: 2
            anchor_title: "center"
    BoxLayout:
        orientation:"vertical"
        spacing: "50dp"
        padding: "20dp"
        adaptive_height: True
        background_color:'Teal'
        pos_hint:{'center_x':0.5,'center_y':0.4}
        size_hint:(0.7,0.7)

    Image:
        source: "What-is-PTSD.png"
        size_hint: 0.9, 0.5
        pos_hint: {"center_x": 0.5, "center_y":0.6}
    MDFillRoundFlatButton:
        text:"Home"
        on_release:root.manager.current='module' 
    MDLabel:
        text:"Post traumatic Stress Disorder (PTSD) is caused by witnessing,experiencing, or learning about someone close to you who experienced traumatic events (such as actual or threatened death,serious injury, or sexual violence)."
        pos_hint: {"center_x": 0.5, "center_y": 0.47}
        halign: "left"
        font_size: "13sp"
        padding:[20,0]
    MDLabel:
        text: "PTSD includes 4 types of symptoms:"
        pos_hint: {"center_x": 0.5, "center_y": 0.39}
        halign: "left"
        font_size: "13sp"
        padding:[20,0]
    MDLabel:
        text: "1. Re-experiencing or reliving the trauma, such as:" 
        pos_hint: {"center_x": 0.5, "center_y": 0.36}  
        halign: "left"
        font_size: "13sp"
        padding:[20,0]
    MDLabel:
        text: "* Disturbing memories or nightmares"
        pos_hint: {"center_x": 0.5, "center_y": 0.33}  
        halign: "left"
        font_size: "13sp"
        padding:[20,0]
    MDLabel:
        text: "* Feeling or acting like the trauma is happening again (flashbacks)"
        pos_hint: {"center_x": 0.5, "center_y": 0.29}  
        halign: "left"
        font_size: "13sp"
        padding:[20,0]
    MDLabel:
        text: "* Becoming very upset when reminded of the trauma"
        pos_hint: {"center_x": 0.5, "center_y": 0.25}  
        halign: "left"
        font_size: "13sp"
        padding:[20,0]
    MDLabel:
        text: "2. Persistent avoidance such as:"
        pos_hint: {"center_x": 0.5, "center_y": 0.21}  
        halign: "left"
        font_size: "13sp"
        padding:[20,0]
    MDLabel:
        text: " *Avoiding memories or thoughts about the trauma"
        pos_hint: {"center_x": 0.5, "center_y": 0.18}  
        halign: "left"
        font_size: "13sp"
        padding:[20,0]
    MDFillRoundFlatButton:
        text:"Home"
        on_release:root.manager.current='module'
    MDLabel:
        text:"* Avoiding thoughts, feelings, or memories closely associated with traumatic events."
        pos_hint:{'center_x':0.5,'center_y':0.14}  
        halign: "left"
        font_size: "13sp"
        padding:[20,0]
    MDLabel:
        text:"3. Negative thoughts and moods"
        pos_hint:{'center_x':0.5,'center_y':0.10}  
        halign: "left"
        font_size: "13sp"
        padding:[20,0]
    
    MDLabel:
        text:"Negative beliefs (such as 'I'm a bad person','I can't trust anyone')"
        pos_hint:{'center_x':0.5,'center_y':0.05}  
        halign: "left"
        font_size: "13sp"
        padding:[20,0]
<Q2>:
    name: "q2"
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'
        MDTopAppBar:
            title: "[i]PTSD Facts[/i]"
            specific_text_color: "white"
            elevation: 2
            anchor_title: "center"
    BoxLayout:
        orientation:"vertical"
        spacing: "50dp"
        padding: "20dp"
        adaptive_height: True
        background_color:'Teal'
        pos_hint:{'center_x':0.5,'center_y':0.4}
        size_hint:(0.7,0.7)
    Image:
        source: "ptsdFacts.png"
        size_hint: 0.9, 0.9
        pos_hint: {"center_x": 0.5, "center_y": 0.7}
    MDFillRoundFlatButton:
        text:"Home"
        on_release:root.manager.current='module' 
    MDFillRoundFlatButton:
        text:"Home"
        on_release:root.manager.current='module'
    MDLabel:
        text:"PTSD is Treatable"
        pos_hint: {"center_x": 0.5, "center_y": 0.58}
        halign: "center"
        font_size: "16sp"
        padding:[20,0]
    MDLabel:
        text:"No matter how long you have lived with PTSD, there are treatments that can help."
        pos_hint: {"center_x": 0.5, "center_y": 0.53}
        halign: "left"
        font_size: "13sp"
        padding:[20,0]
    MDLabel:
        text:"Treatment Helps"
        pos_hint: {"center_x": 0.5, "center_y": 0.45}
        halign: "center"
        font_size: "16sp"
        padding:[20,0]
    MDLabel:
        text:"Talking to a professional is one of the best things you can do to help with PTSD. There are several evidence-based treatments that have been shown to be effective in reducing PTSD symptoms."
        pos_hint: {"center_x": 0.5, "center_y": 0.37}
        halign: "left"
        font_size: "13sp"
        padding:[20,0]
    MDLabel:
        text:"Did You Know?"
        pos_hint: {"center_x": 0.5, "center_y": 0.28}
        halign: "center"
        font_size: "16sp"
        padding:[20,0]
    MDLabel:
        text:"Over 600,000 Veterans who used VA services as recently as 2016 were diagnosed with PTSD."
        pos_hint: {"center_x": 0.5, "center_y": 0.23}
        halign: "left"
        font_size: "13sp"
        padding:[20,0]
    MDLabel:
        text:"For those in infantry units that experienced combat, 13 out of every 100 Service Members had PTSD."
        pos_hint: {"center_x": 0.5, "center_y": 0.17}
        halign: "left"
        font_size: "13sp"
        padding:[20,0]
    MDLabel:
        text:"5 out of every 100 active duty Service Members were estimated to have PTSD after deployment."
        pos_hint: {"center_x": 0.5, "center_y": 0.10}
        halign: "left"
        font_size: "13sp"
        padding:[20,0]
<Q3>:
    name: "q3"
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'
        MDTopAppBar:
            title: "[i]How does PTSD develop?[/i]"
            specific_text_color: "white"
            elevation: 2
            anchor_title: "center"
    BoxLayout:
        orientation:"vertical"
        spacing: "50dp"
        padding: "20dp"
        adaptive_height: True
        background_color:'Teal'
        pos_hint:{'center_x':0.5,'center_y':0.4}
        size_hint:(0.7,0.7)
    Image:
        source: "ptsdDevelop.png"
        size_hint: 0.9, 0.9
        pos_hint: {"center_x": 0.5, "center_y": 0.7}
    MDFillRoundFlatButton:
        text:"Home"
        on_release:root.manager.current='module' 
    MDFillRoundFlatButton:
        text:"Home"
        on_release:root.manager.current='module'
    MDLabel:
        text:"After trauma, it's normal to be in shock, have painful memories, and be upset by reminders. Trauma can also change how people think about themselves, others, and the world to more extreme ideas like  'nowhere is safe, 'or' no one can be trusted'."
        pos_hint: {"center_x": 0.5, "center_y": 0.45}
        halign: "left"
        font_size: "13sp"
        padding:[20,0]
    MDLabel:
        text:"For most, these reactions will lessen over time. But for some, these reactions continue and can be severe enough to disturb everyday life."
        pos_hint: {"center_x": 0.5, "center_y": 0.30}
        halign: "left"
        font_size: "13sp"
        padding:[20,0]
           
<Welcome>:
    name:"Welcome"
    MDLabel:
        text:'Hello There!Welcome to Chitta-The Inner You!We are glad you choose us. Together let us navigate this complex yet insteresting journey called life!'
        
        
        font_size: 30
        padding:[40,0]
        markup:True
        theme_text_color:'Custom'
        text_color:(0/ 255.0, 128/ 255.0, 128 / 255.0, 1)
        font_style:'Subtitle1'
        pos_hint:{"center_x":0.5,"center_y":0.6}
        
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'
        # orientation:'vertical'
        MDTopAppBar:
            title: "[i]CHITTA[/i]"
            
            specific_text_color: "white"
            elevation: 2
            anchor_title: "center"
            
            
            
    MDFillRoundFlatButton:
        text:"Continue"
        pos_hint:{'center_x': 0.5, 'center_y': 0.3}
        on_release:root.manager.current='disclaimer'
        
<Disclaimer>:
    
    name:"disclaimer"
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'
        MDTopAppBar:
            title: "[i]Disclaimer[/i]"
            specific_text_color: "white"
            elevation: 2
            anchor_title: "center"
            markup:True
    MDLabel
        text:'[i]The content of this application is intended for use only as an informative tool. It is not intended to be, and shoulld not be used in any way as a substitute for professional medical advice or training.The accuracy of the information provided is not guaranteed.The user acknowledges in initiating this application that the information is not meant to develop a health treatment plan.If you are in an emergency or life -threatening medical situation, seek medical assistance immediately[/i]'
        size_hint: 1,0.10
        pos:20,300
        font_size: 20
        padding:[40,0]
        markup:True
        theme_text_color:'Custom'
        text_color:(0/ 255.0, 128/ 255.0, 128 / 255.0, 1)
        font_style:'Subtitle1'
    
    MDFillRoundFlatButton:
        text:"Tap to Accept"
        pos_hint:{'center_x': 0.5, 'center_y': 0.2}
        on_release:root.manager.current='module'
        
<Module>:
    name:'module'
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'
        MDTopAppBar:
            title: "[i]Home[/i]"
            specific_text_color: "white"
            elevation: 2
            anchor_title: "center"
            markup:True
            
    MDFillRoundFlatButton:
        text:"Manage Symptoms"
        pos_hint:{'center_x': 0.5, 'center_y': 0.8}
        size_hint:(0.5, 0.2)
        on_release:root.manager.current='symptoms_list'
    MDFillRoundFlatButton:
        text:"Learn"
        pos_hint:{'center_x': 0.5, 'center_y': 0.5}
        size_hint:(0.5, 0.2)
        on_release:root.manager.current='learn_list'
    MDFillRoundFlatButton:
        text:"Get Support"
        pos_hint:{'center_x': 0.5, 'center_y': 0.2}
        size_hint:(0.5, 0.2)
        on_release:root.manager.current='get_support'
        
   
            
<LearnList>:  
    name:"learn_list"
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'
        MDTopAppBar:
            title: "[i]Learn[/i]"
            specific_text_color: "white"
            elevation: 2
            anchor_title: "center"
            left_action_items: [["home", lambda x: root.manager.set_screen('module')]]
            markup:True
    MDFillRoundFlatButton:
        text:"Home"
        on_release:root.manager.current='module'    
    ScrollView:
       
        
        MDList:
            pos_hint: {"center_x": .5, "center_y": .7}
            padding:[40,0]
            pos_hint:{'center_x':0.5,'center_y':0.5}
            OneLineAvatarListItem:
                text:"What is ptsd?"
                source:"What-is-PTSD.png"
                on_release:root.manager.current='q1'
            OneLineAvatarListItem:
                text:"PTSD FACTs"
                source:"ptsdFacts.png"
                on_release:root.manager.current='q2'
            OneLineAvatarListItem:
                text:"How does PTSD develops?"
                source:"ptsdDevelop.png"
                on_release:root.manager.current='q3'
            OneLineAvatarListItem:
                text:"How common is PTSD?"
                source:"commonptsd.png"
                on_release:root.manager.current='q4'
            OneLineAvatarListItem:
                text:"Who develops"
                source:"ptsdDevelop.png"
                on_release:root.manager.current='q5'
            OneLineAvatarListItem:
                text:"How long does PTSD lasts?"
                source:"RT.png"
                on_release:root.manager.current='q6'
            OneLineAvatarListItem:
                text:"Problems related"
                source:"problemPTSD.png"
                on_release:root.manager.current='q7'
<GetSupport>:
    name:'get_support'
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'
        MDTopAppBar:
            title: "[i]Get Support[/i]"
            specific_text_color: "white"
            elevation: 2
            anchor_title: "center"
    MDFillRoundFlatButton:
        text:"Home"
        on_release:root.manager.current='module'
    MDFillRoundFlatButton:
        text:"Crisis Resources"
        pos_hint:{'center_x': 0.5, 'center_y': 0.5}
        size_hint:(0.5, 0.2)
        on_release:root.manager.current='crisisresources'
    MDFillRoundFlatButton:
        text:"Find Professional Care"
        pos_hint:{'center_x': 0.5, 'center_y': 0.2}
        size_hint:(0.5, 0.2)
        on_release: root.open_maps('therapy near me')
      
    MDFillRoundFlatButton:
        text:"Home"
        on_release:root.manager.current='module'
<CrisisResources>:
    name:"crisisresources"
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'
        MDTopAppBar:
            title: "[i]Crisis Resources[/i]"
            specific_text_color: "white"
            elevation: 2
            anchor_title: "center"
    BoxLayout:
        orientation:"vertical"
        spacing: "50dp"
        padding: "20dp"
        adaptive_height: True
        background_color:'Teal'
        pos_hint:{'center_x':0.5,'center_y':0.4}
        size_hint:(0.7,0.7)
    MDLabel:
        text:"National Suicide Prevention Lifeline:"
        size_hint: 1,0.10
        pos:35,450
        font_size: 15
    MDLabel:
        text:"National Domestic Violence Hotline :"
        size_hint: 1,0.10
        pos:40,310
        font_size: 15
    MDLabel:
        text:"National Sexual Assault Hotline:"
        padding:[40,0]
        pos:10,150
        size_hint: 1,0.10
        font_size: 15


    MDFillRoundFlatButton:
        text:"Back"
        pos:30,30
        on_release:root.manager.current='get_support'

    MDFillRoundFlatButton:
        text:"call 9152987821"
        pos:100,420
        background_color:(0/ 255.0, 128/ 255.0, 128 / 255.0, 1)
        # on_press: self.sucide()

    MDFillRoundFlatButton:
        text:"call 8793088814"
        pos:100,280
        # on_press: self.domestic()
       

    MDFillRoundFlatButton:
        text:"call 7827170170"
        pos:100,120
        # on_press: self.sexual()
        
    
    
            



        

        
<SymptomsList> :  
    name:"symptoms_list"
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'
        MDTopAppBar:
            title: "[i]Symptoms[/i]"
            anchor_title: "left"
            specific_text_color: "white"
            elevation: 2
            left_action_items: [["home", lambda x: root.manager.set_screen('module')]]
            anchor_title: "center"
    MDFillRoundFlatButton:
        text:"Home"
        on_release:root.manager.current='module'
    ScrollView:
        
        
        MDList:
            pos_hint: {"center_x": .5, "center_y": .7}
            padding:[40,0]
            
            OneLineAvatarListItem:
                text:"Unable to sleep"
                
                source:"unabletosleep.png"
                
                on_release:root.manager.current='distress_meterUTS'
                
                
                pos_hint:{'center_x':0.5,'center_y':0.5}
            OneLineAvatarListItem:
                text:"Worried/Anxiety"
                source:"worried.png"
                on_release:root.manager.current='distress_meterW'
            OneLineAvatarListItem:
                text:"Hopeless/Sad"
                source:"sad.png"
                on_release:root.manager.current='distress_meterS'
            OneLineAvatarListItem:
                text:"Difficulty in Concentrating"
                source:"D.png"
                on_release:root.manager.current='distress_meterD'
            OneLineAvatarListItem:
                text:"Avolding Triggers"
                source:"at.png"
                on_release:root.manager.current='distress_meterA'
            OneLineAvatarListItem:
                text:"Reminded Trauma"
                source:"RT.png"
                on_release:root.manager.current='distress_meterRT'
            OneLineAvatarListItem:
                text:"Angry"
                source:"angry.png"
                on_release:root.manager.current='distress_meterangre'
<Connect>:
    name: "connect"
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'
        MDTopAppBar:
            title: "[i]Connect[/i]"
            specific_text_color: "white"
            elevation: 2
            anchor_title: "center"
    BoxLayout:
        orientation:"vertical"
        spacing: "50dp"
        padding: "20dp"
        adaptive_height: True
        background_color:'Teal'
        pos_hint:{'center_x':0.5,'center_y':0.4}
        size_hint:(0.7,0.7)
    Image:
        source: "connect.png"
        size_hint: 0.9, 0.3
        pos_hint: {"center_x": 0.5, "center_y": 0.7}
    MDLabel:
        text:"It can help to get support from trusted people when experiencing physical and emotional symptoms of stress. Talking to another person your problems, or listening to someone else's problems for a while, can help improve your mood or change the way think. Try this:"
        pos_hint: {"center_x": 0.5, "center_y": 0.45}
        halign: "left"
        font_size: "13sp"
        padding:[20,0]
    MDFillRoundFlatButton:
        text:"Home"
        on_release:root.manager.current='module' 
    MDLabel:
        text:"*.Call a family member"
        pos_hint: {"center_x": 0.5, "center_y": 0.38}
        halign: "center"
        font_size: "13sp"
        padding:[20,0]
    MDLabel:
        text:"*.Call a friend"
        pos_hint: {"center_x": 0.5, "center_y": 0.33}
        halign: "center"
        font_size: "13sp"
        padding:[20,0]
    MDLabel:
        text:"*.Cook dinner for someone"
        pos_hint: {"center_x": 0.5, "center_y": 0.3}
        halign: "center"
        font_size: "13sp"
        padding:[20,0]
    MDLabel:
        text:"*.Go to a party"
        pos_hint: {"center_x": 0.5, "center_y": 0.25}
        halign: "center"
        font_size: "13sp"
        padding:[20,0]
    MDLabel:
        text:"*.Make a small gift for someone"
        pos_hint: {"center_x": 0.5, "center_y": 0.2}
        halign: "center"
        font_size: "13sp"
        padding:[20,0]
    MDFillRoundFlatButton:
        text:"Home"
        on_release:root.manager.current='module'
<Inspiring>:
    name: "inspiring"
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'
        MDTopAppBar:
            title: "[i]Inspiring Quotes[/i]"
            specific_text_color: "white"
            elevation: 2
            anchor_title: "center"
    BoxLayout:
        orientation:"vertical"
        spacing: "50dp"
        padding: "20dp"
        adaptive_height: True
        background_color:'Teal'
        pos_hint:{'center_x':0.5,'center_y':0.4}
        size_hint:(0.7,0.7)
    Image:
        source: "inspiring.png"
        size_hint: 0.9, 0.3
        pos_hint: {"center_x": 0.5, "center_y": 0.7}
    MDFillRoundFlatButton:
        text:"Home"
        on_release:root.manager.current='module' 
    MDLabel:
        text:"*. Although the world is full of suffering, it is full also of the overcoming of it."
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        halign: "left"
        font_size: "13sp"
        padding:[20,0]
    MDLabel:
        text:"*. You are not responsible for being down,but you are responsible for getting up."
        pos_hint: {"center_x": 0.5, "center_y": 0.4}
        halign: "left"
        font_size: "13sp"
        padding:[20,0]
    MDLabel:
        text:"*. And the trouble is , if you don't risk anything, you risk even more."
        pos_hint: {"center_x": 0.5, "center_y": 0.3}
        halign: "left"
        font_size: "13sp"
        padding:[20,0]
    MDLabel:
        text:"*. You yourself, as much as anybody in th entire universe,deserve your love and affection"
        pos_hint: {"center_x": 0.5, "center_y": 0.2}
        halign: "left"
        font_size: "13sp"
        padding:[20,0]
    MDFillRoundFlatButton:
        text:"Home"
        on_release:root.manager.current='module'
<Soothing>:
    name: "soothing"
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'
        MDTopAppBar:
            title: "[i]Soothing[/i]"
            specific_text_color: "white"
            elevation: 2
            anchor_title: "center"
    BoxLayout:
        orientation:"vertical"
        spacing: "50dp"
        padding: "20dp"
        adaptive_height: True
        background_color:'Teal'
        pos_hint:{'center_x':0.5,'center_y':0.4}
        size_hint:(0.7,0.7)
    Image:
        source: "soothing.png"
        size_hint: 0.9, 0.3
        pos_hint: {"center_x": 0.5, "center_y": 0.7}
    MDFillRoundFlatButton:
        text:"Home"
        on_release:root.manager.current='module' 
    MDLabel:
        text:"Look at a picture that is meaningful or soothing you ......."
        pos_hint: {"center_x": 0.5, "center_y": 0.45}
        halign: "left"
        font_size: "13sp"
        padding:[20,0]
    MDFillRoundFlatButton:
        text:"Home"
        on_release:root.manager.current='module'
<MuscleRelax>:
    name: 'musclerelax'
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'
        MDTopAppBar:
            title: "[i]Muscle Relaxation[/i]"
            specific_text_color: "white"
            elevation: 2
            anchor_title: "center"
            left_action_items: [["home", lambda x: root.manager.set_screen('module')]]
            markup:True
    MDFillRoundFlatButton:
        text:"Home"
        on_release:root.manager.current='module'    
    MDLabel:
        text:"You are about to be lead through a progressiv muscle relaxation excercise. You will progress through each of your major muscle groups, tensing and relaxing as you go. This excercise takes about 9 minutes(approx). It has accompaning audio, so you will need to find a quiet place or put your headphones now."
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        halign: "left"
        font_size: "13sp"
        padding:[20,0]
    MDLabel:
        text:"Sit down in a comfortable chair or laydown. Do not do this excercise while driving."
        pos_hint: {"center_x": 0.6, "center_y": 0.45}
        halign: "left"
        font_size: "13sp"
        padding:[20,0]
    MDRaisedButton:
        text: "Start"
        on_release: root.play_music()
        pos_hint: {"center_x": 0.5, "center_y": 0.3}
    MDRaisedButton:
        text: "Stop"
        pos_hint: {"center_x": 0.5, "center_y": 0.2}
        on_release: root.stop_music()
    MDFillRoundFlatButton:
        text:"Home"
        on_release:root.manager.current='module'
    
            
        

    
   
            
""")


class Quote(Screen):
    pass


class Welcome(Screen):
    pass


class Que1_Example(Screen):
    pass


class Disclaimer(Screen):
    pass


class LearnList(Screen):
    pass
class Connect(Screen):
    pass
class Q1(Screen):
    pass
class Q2(Screen):
    pass
class Q3(Screen):
    pass
class Q4(Screen):
    pass
class Q5(Screen):
    pass
class Q6(Screen):
    pass
class Q7(Screen):
    pass
class Grounding(Screen):
    pass
class DeepBreath(Screen):
    pass
class Soothing(Screen):
    pass






class GetSupport(Screen):
    def open_maps(self, place):
        android.start_app('geo:0,0?q=' + place)


class Progress(Screen):
    pass
class Distress_meterUnableToSleep(Screen):
    pass
class Distress_meterWorried(Screen):
    pass
class Distress_meterSAD(Screen):
    pass
class Distress_meterDifficulty(Screen):
    pass
class Distress_meterAvoiding(Screen):
    pass
class Distress_meterReminded(Screen):
    pass
class Distress_meterAngry(Screen):
    pass
class Inspiring(Screen):
    pass
class MuscleRelax(Screen):

    def on_start(self):
        self.sound = SoundLoader.load('mucle.mp3')

    def play_music(self):
        if hasattr(self,'sound')and self.sound:
            self.sound.play()

    def stop_music(self):
        if hasattr(self,'sound')and self.sound:
            self.sound.stop()
class PlayMusicScreen(Screen):
    def birds(self):
        sound = SoundLoader.load('birds.mp3')
        if sound:
            sound.play()
    def waterfall(self):
        sound = SoundLoader.load('waterfall.mp3')
        if sound:
            sound.play()
    def stream(self):
        sound = SoundLoader.load('stream.mp3')
        if sound:
            sound.play()
    def flute(self):
        sound = SoundLoader.load('flute.mp3')
        if sound:
            sound.play()



class SymptomsList(Screen):
    pass

class CrisisResources(Screen):
    def domestic(self):
        PythonActivity = autoclass('org.kivy.android.PythonActivity')
        Intent = autoclass('android.content.Intent')
        Uri = autoclass('android.net.Uri')
        intent = Intent(Intent.ACTION_CALL)
        intent.setData(Uri.parse('tel:+918793088814'))
        currentActivity = PythonActivity.mActivity
        currentActivity.startActivity(intent)
    def sucide(self):
        PythonActivity = autoclass('org.kivy.android.PythonActivity')
        Intent = autoclass('android.content.Intent')
        Uri = autoclass('android.net.Uri')
        intent = Intent(Intent.ACTION_CALL)
        intent.setData(Uri.parse('tel:+919152987821'))
        currentActivity = PythonActivity.mActivity
        currentActivity.startActivity(intent)
    def sexual(self):
        PythonActivity = autoclass('org.kivy.android.PythonActivity')
        Intent = autoclass('android.content.Intent')
        Uri = autoclass('android.net.Uri')
        intent = Intent(Intent.ACTION_CALL)
        intent.setData(Uri.parse('tel:+917827170170'))
        currentActivity = PythonActivity.mActivity
        currentActivity.startActivity(intent)
class Que1(Screen):
    pass


class Module(Screen):
    pass



class Q(Screen):
    pass


class ScreenManagement(ScreenManager):
    pass


sm = ScreenManager()
sm.add_widget(Quote(name='Chitta'))
sm.add_widget(Welcome(name='Welcome'))
sm.add_widget(Disclaimer(name='disclaimer'))
sm.add_widget(Module(name='module'))
sm.add_widget(LearnList(name='learn_list'))
sm.add_widget(Progress(name='Track_progress'))
sm.add_widget(LearnList(name='learn_list'))
sm.add_widget(GetSupport(name='get_support'))
sm.add_widget(Q1(name='q1'))
sm.add_widget(Q2(name='q2'))
sm.add_widget(Q6(name='q6'))
sm.add_widget(Q7(name='q7'))
sm.add_widget(Q3(name='q3'))
sm.add_widget(Q4(name='q4'))
sm.add_widget(Q5(name='q5'))
sm.add_widget(Grounding(name='grounding'))
sm.add_widget(DeepBreath(name='deep breath'))
sm.add_widget(Connect(name='connect'))
sm.add_widget(Soothing(name='soothing'))
sm.add_widget(Inspiring(name='inspiring'))
sm.add_widget(CrisisResources(name='crisisresources'))


class main(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.primary_hue = '400'

        screen = Builder.load_string(screen_helper)

        return screen


if __name__ == '__main__':
    main().run()
