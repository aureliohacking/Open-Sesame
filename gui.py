gui = """
BoxLayout:
    orientation:'vertical'

    MDToolbar:
        title: 'Definitivas U'
        # md_bg_color: .17, .66, .66, 1
        # specific_text_color: .66, .17, .17, 1

    MDBottomNavigation:
        # panel_color: .2, .2, .2, 1

        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'Cálculo'
            icon: 'calculator'
   

            GridLayout:
                size_hint: 1, 1
                cols: 1

                MDLabel:
                    text: "Calcula tu definitiva"
                    halign: "center"
                    font_style: 'H5'


                AnchorLayout:
                    anchor_x: 'center'
                    size_hint_y: None
                    height: "60dp"
                    
                    MDTextField:
                        hint_text: "Primer corte"
                        icon_right: "numeric-1-box-outline"
                        icon_right_color: app.theme_cls.primary_color
                        helper_text: "Use . para notación decimal"
                        helper_text_mode: "on_focus"
                        size_hint: None, None
                        width: "220dp"
                        id: nota1
                    

                AnchorLayout:
                    anchor_x: 'center'
                    size_hint_y: None
                    height: "60dp"
                    
                    MDTextField:
                        hint_text: "Segundo corte"
                        icon_right: "numeric-2-box-outline"
                        icon_right_color: app.theme_cls.primary_color
                        helper_text: "Use . para notación decimal"
                        helper_text_mode: "on_focus"
                        size_hint: None, None
                        width: "220dp"
                        id: nota2


                AnchorLayout:
                    anchor_x: 'center'
                    size_hint_y: None
                    height: "60dp"
                    
                    MDTextField:
                        hint_text: "Tercer corte"
                        icon_right: "numeric-3-box-outline"
                        icon_right_color: app.theme_cls.primary_color
                        helper_text: "Use . para notación decimal"
                        helper_text_mode: "on_focus"
                        size_hint: None, None
                        width: "220dp"    
                        id: nota3 


                AnchorLayout:
                    anchor_x: 'center'
                    size_hint_y: None
                    height: "60dp"
                    
                    MDRaisedButton:
                        text: "Calcular"
                        on_press: app.calc_nota(nota1.text, nota2.text, nota3.text)


                AnchorLayout:
                    anchor_x: 'center'
                    size_hint_y: None
                    height: "60dp"
                    
                    MDLabel:
                        id: notafinal
                        text: ""
                        halign: "center"                       

                                                           


        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'Configuración'
            icon: 'settings-outline'

            GridLayout:
                size_hint: 1, 1
                cols: 1


                MDLabel:
                    text: "Cambiar ponderación"
                    halign: "center"
                    font_style: 'H5'  
                    size_hint: 1, None               


                AnchorLayout:
                    anchor_x: 'center'
                    size_hint_y: None
                    height: "60dp"
                    
                    MDTextField:
                        hint_text: "Porcentaje Primer corte"
                        icon_right: "percent-outline"
                        icon_right_color: app.theme_cls.primary_color
                        helper_text: "No use el signo de porcentaje, solo el valor"
                        helper_text_mode: "on_focus"
                        size_hint: None, None
                        width: "220dp"
                        id: corte1
                        text: "35"
                    

                AnchorLayout:
                    anchor_x: 'center'
                    size_hint_y: None
                    height: "60dp"
                    
                    MDTextField:
                        hint_text: "Porcentaje Segundo corte"
                        icon_right: "percent-outline"
                        icon_right_color: app.theme_cls.primary_color
                        helper_text: "No use el signo de porcentaje, solo el valor"
                        helper_text_mode: "on_focus"
                        size_hint: None, None
                        width: "220dp"
                        id: corte2
                        text: "35"


                AnchorLayout:
                    anchor_x: 'center'
                    size_hint_y: None
                    height: "60dp"
                    
                    MDTextField:
                        hint_text: "Porcentaje Tercer corte"
                        icon_right: "percent-outline"
                        icon_right_color: app.theme_cls.primary_color
                        helper_text: "No use el signo de porcentaje, solo el valor"
                        helper_text_mode: "on_focus"
                        size_hint: None, None
                        width: "220dp"    
                        id: corte3
                        text: "30" 

"""