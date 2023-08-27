#!/usr/bin/python
# -*- coding: UTF-8 -*-
# --------------------------------------------------------- #
#                    MY SOFTWARE GROUP                      #
# --------------------------------------------------------- #
# @Author       :    Ares.He
# @Mail         :    502614708@qq.com
# @Date         :    2023/8/25
# @Revision     :    1.0.0
# @File         :    Main.py
# @Software     :    PyCharm
# @Usefor       :    
# --------------------------------------------------------- #

_header = {
    'description': '''
    -> 本程序任何其他团体或个人如需使用，必须经作者的批准，并遵守以下约定；
    1> 本着尊重创作者的劳动成果，任何团体或个人在使用此程序的时候，均需要知会此程序的原始创作者；
    2> 在任何场合宣导、宣传，在任何文件、报告、邮件中提及本程序的全部或部分功能，均需要声明此程序的
       原始创作者；
    3> 在任何时候对本程序做部分修改或者是升级时，必须要保留文件的原始信息，包括原始文件名、创作者及
       联系方式、创作日期等信息，且不得删除程序中的源代码，只能进行注释处理；
'''
}
'''
                   _ooOoo_
                  o8888888o
                  88" . "88
                  (| -_- |)
                  O\  =  /O
               ____/`---'\____
             .'  \\|     |//  `.
            /  \\|||  :  |||//  \
           /  _||||| -:- |||||-  \
           |   | \\\  -  /// |   |
           | \_|  ''\---/''  |   |
           \  .-\__  `-`  ___/-. /
         ___`. .'  /--.--\  `. . __
      ."" '<  `.___\_<|>_/___.'  >'"".
     | | :  `- \`.;`\ _ /`;.`/ - ` : | |
     \  \ `-.   \_ __\ /__ _/   .-` /  /
======`-.____`-.___\_____/___.-`____.-'======
                   `=---='
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
           佛祖保佑       永无BUG
'''
import os, sys, platform, re, math, shutil
from datetime import datetime
import time
from PyQt5 import QtCore, QtGui, QtWidgets
#--设置包路径,适用于直接运行源码,打包必须将包放到当前目录
if platform.system() == "Windows":
    # scriptPath = "%s/sys/scripts" % os.environ.get('SCRIPTS_DIR', '//10.110.65.128/incam/genesis')
    # --新增windows包路径
    sys.path.insert(0, "\\\\192.168.17.61\\扫描文件\\暂时不要删除--刘才林\\pythonEnv\\Package")
    sys.path.insert(0, "F:\\Python\\Package")
else:
    # scriptPath = "%s/scripts" % os.environ.get('SCRIPTS_DIR', '/genesis/output/incam/genesis')
    # --新增linux包路径
    sys.path.insert(0, "/incam/server/site_data/Package")
import genCOM_36 as genCOM
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QMessageBox
import ui.win as win
import ui.icon

class MAIN():
    def __init__(self):
        self.GEN = genCOM.GEN_COM()
        self.JOB = os.environ.get("JOB")
        self.STEP = os.environ.get("STEP")
        self.checkProgramTime()

    def checkProgramTime(self, filePath='C:\\Windows\\v.time.txt'):
        '''
        检查程序到期时间
        :param filePath:
        :return:
        '''

        '''
        if os.path.exists(filePath):
            with open(filePath,'r') as f:
                tTime = int(f.readline())
                lTime = int(time.strftime("%Y%m%d", time.localtime()))
                if tTime < lTime:
                    self.message('warning', '系统提示', '程序时间已到期,请联系管理人员!!!')
                    sys.exit(0)
        '''

        if int(time.strftime("%Y%m%d", time.localtime())) > 20231230:
            self.message('warning', '系统提示', '程序时间已到期,请联系管理人员!!!')
            sys.exit(0)

    def setWindows(self):
        '''
        设定界面参数
        :return:
        '''
        self.MainWindow = QtWidgets.QWidget()
        self.ui = win.Ui_Form()
        self.ui.setupUi(self.MainWindow)
        # --设置置顶
        self.MainWindow.setWindowFlags(QtCore.Qt.WindowType.WindowStaysOnTopHint)
        self.MainWindow.show()
        # self.setVcutInfo()
        self.setSteps()
        self.setBasePath()
        self.fun_slot()
        # self.setOtherSlot()

    def setVcutInfo(self):
        '''
        设置vcut界面基本参数
        :return:
        '''
        self.ui.selAuthor.setText(self.GEN.getUser())
        self.ui.residualThickness.setText('0.6')

    def setSteps(self):
        '''

        :return:
        '''

        # --设定当前step
        # self.ui.currentStep.addItems([self.STEP])
        mapSteps = []
        vcutSteps = []
        holeMapSteps = []
        info = self.GEN.DO_INFO('-t job -e {0} -m script -d STEPS_LIST'.format(self.JOB))
        for s in info['gSTEPS_LIST']:
            if re.search(re.compile('^edit|set'), s):
                mapSteps.append(s)
                holeMapSteps.append(s)
            elif re.search(re.compile('^pnl'), s):
                vcutSteps.append(s)

        self.ui.mapStep.addItems(mapSteps)
        self.ui.mapStep.setCurrentIndex(len(mapSteps) - 1)
        # self.ui.holeStep.addItems(mapSteps)
        # self.ui.holeStep.setCurrentIndex(len(mapSteps)-1)
        # self.ui.vcutStep.addItems(vcutSteps)

    def setBasePath(self):
        '''
        设置输出路径
        :param selSite:工厂
        :param STATUS:状态
        :return:
        '''

        self.defPath = 'd:\\disk'
        self.ui.outputPath.setText(self.defPath)

    def setOtherSlot(self):
        '''
        设定其他控件
        :return:
        '''

        """
        checkbox 0不选择 2选择 1半选中
        """
        # if self.GEN.LAYER_EXISTS('v-cut') == 'yes':
        #     self.ui.createVcut.setCheckState(2)

        # --客户要求取消默认选项
        # self.ui.deleteNote.setCheckState(2)
        # self.ui.mapNote.setCheckState(2)
        # self.ui.map2pdf.setCheckState(2)

        pass

    def fun_slot(self):
        '''
        信号绑定
        :return:
        '''

        self.ui.runProgram.clicked.connect(self.runScripts)
        self.ui.exitProgram.clicked.connect(sys.exit)
        self.ui.selPath.clicked.connect(self.setOutputPath)

    def setOutputPath(self):
        '''
        选择输出路径
        :return:
        '''

        # if platform.system() != "Windows":
        #     return
        # --创建一个窗口
        win = QWidget()
        path = QtWidgets.QFileDialog.getExistingDirectory(win, '请选择保存目录', self.defPath)
        if path:
            self.ui.outputPath.setText(path)

    def runScripts(self):
        '''
        运行脚本
        :return:
        '''

        '''
        data = {
            'map2pdf':self.ui.map2pdf.isChecked(),
            'mapNote':self.ui.mapNote.isChecked(),
            'createHoleMap':self.ui.createHoleMap.isChecked(),
            'createVcut':self.ui.createVcut.isChecked(),
            'vcut2pdf':self.ui.vcut2pdf.isChecked(),
            'deleteNote':self.ui.deleteNote.isChecked(),
            'boardThick':self.ui.selBoardThick.text(),
            'currentStep':self.ui.currentStep.currentText(),
            'mapStep':self.ui.mapStep.currentText(),
            'holeStep':self.ui.holeStep.currentText(),
            'vcutStep':self.ui.vcutStep.currentText(),
            'selAuthor':self.ui.selAuthor.text().upper(),
            'residualThickness':self.ui.residualThickness.text(),
            'routTol':self.ui.routTol.text(),
            'vcutMode':self.ui.vcutMode.currentText(),
            'vcutAngle':self.ui.vcutAngle.currentText(),
            'outputPath':self.ui.outputPath.text(),
        }'''
        data = {
            'map2pdf': self.ui.map2pdf.isChecked(),
            'mapNote': self.ui.mapNote.isChecked(),
            'deleteNote': self.ui.deleteNote.isChecked(),
            # 'currentStep': self.ui.currentStep.currentText(),
            'mapStep': self.ui.mapStep.currentText(),
            'outputPath': self.ui.outputPath.text(),
        }

        self.MainWindow.close()
        W = OUTPUT(data)
        W.startScripts()
        self.message('warning', '系统提示', '脚本运行完成!!!')
        sys.exit()

    def message(self, messageType, messageTitle, messageContent):
        '''
        message提示信息
        :param messageType: 提示类型
        :param messageTitle: 提示抬头
        :param messageContent: 提示内容
        :return:
        '''

        if messageType == 'info':
            msg_box = QMessageBox(QMessageBox.Information, messageTitle, messageContent)
            msg_box.exec_()
        elif messageType == 'warning':
            msg_box = QMessageBox(QMessageBox.Warning, messageTitle, messageContent)
            msg_box.exec_()


class OUTPUT():
    def __init__(self, data):
        self.GEN = genCOM.GEN_COM()
        self.JOB = os.environ.get("JOB")
        self.STEP = os.environ.get("STEP")
        self.outline = 'map'

        """
         data = {
            'map2pdf':self.ui.map2pdf.isChecked(),
            'mapNote':self.ui.mapNote.isChecked(),
            'createHoleMap':self.ui.createHoleMap.isChecked(),
            'createVcut':self.ui.createVcut.isChecked(),
            'vcut2pdf':self.ui.vcut2pdf.isChecked(),
            'deleteNote':self.ui.deleteNote.isChecked(),
            'boardThick':self.ui.selBoardThick.text(),
            'currentStep':self.ui.currentStep.currentText(),
            'mapStep':self.ui.mapStep.currentText(),
            'holeStep':self.ui.holeStep.currentText(),
            'vcutStep':self.ui.vcutStep.currentText(),
            'selAuthor':self.ui.selAuthor.text(),
            'residualThickness':self.ui.residualThickness.text(),
            'routTol':self.ui.routTol.text(),
            'vcutMode':self.ui.vcutMode.currentText(),
            'vcutAngle':self.ui.vcutAngle.currentText(),
            'outputPath':self.ui.outputPath.text(),
        }
        """

        '''
        data = {
            'map2pdf': self.ui.map2pdf.isChecked(),
            'mapNote': self.ui.mapNote.isChecked(),
            'deleteNote': self.ui.deleteNote.isChecked(),
            'currentStep': self.ui.currentStep.currentText(),
            'mapStep': self.ui.mapStep.currentText(),
            'outputPath': self.ui.outputPath.text(),
        }
        '''
        self.map2pdf = data['map2pdf']
        self.mapNote = data['mapNote']
        self.deleteNote = data['deleteNote']
        self.outputPath = data['outputPath']
        # self.currentStep = data['currentStep']
        self.mapStep = data['mapStep']

    def startScripts(self):
        '''
        开始运行脚本
        :return:
        '''
        if self.GEN.LAYER_EXISTS(self.outline) != 'yes':
            self.message('warning', '系统提示', '检测不到map层,请创建!')
            sys.exit(0)

        self.GEN.OPEN_STEP(self.mapStep)
        self.GEN.CLEAR_LAYER()
        self.GEN.FILTER_RESET()
        self.GEN.CHANGE_UNITS('mm')

        outData = self.getOutProfile(self.mapStep)
        vcutData = self.getVcut(outData, self.mapStep)
        editSr = self.getEdirSr(outData)

        # if self.creHoleMap:
        #     if self.GEN.LAYER_EXISTS('drl') == 'yes':
        #         self.creHoleMap('drl',self.holeStep,self.boardThick,outData)
        #     else:
        #         self.message('warning', '系统提示', '检测不到drl层存在,分孔图无法制作!!!')

        if self.deleteNote:
            self.GEN.FILTER_RESET()
            self.GEN.WORK_LAYER(self.outline)
            self.GEN.FILTER_TEXT_ATTR('.bit', 'map')
            self.GEN.FILTER_SELECT()
            if int(self.GEN.GET_SELECT_COUNT()) > 0:
                self.GEN.SEL_DELETE()
            self.GEN.FILTER_RESET()

        if self.mapNote:
            self.otherNote(outData, editSr, vcutData)

            self.message('warning', '系统提示', '请选择需要标注物件【选内槽】')
            self.GEN.FILTER_RESET()
            self.GEN.WORK_LAYER(self.outline)
            # print (self.GEN.MOUSE('please select...','p'))
            self.GEN.PAUSE('Please select...')
            if int(self.GEN.GET_SELECT_COUNT()) > 0:
                #     self.message('warning', '警告信息', '检测到未选择物件!!!')
                # else:
                self.analyseOut()
            self.message('warning', '系统提示', '请选择需要单独标注物件【点选两条线】')
            self.selectTwoLine(outData)

        # if self.currentStep != self.mapStep:
        #     self.GEN.CLOSE_STEP()

        # if self.createVcut:
        #     self.createVcutMap(vcutData)
        #     if self.currentStep != self.vcutStep:
        #         self.GEN.CLOSE_STEP()

        if self.map2pdf:
            self.GEN.OPEN_STEP(self.mapStep)
            self.outputPdf(self.outline)
            # if self.currentStep != self.mapStep:
            #     self.GEN.CLOSE_STEP()
        # if self.vcut2pdf:
        #     self.GEN.OPEN_STEP(self.vcutStep)
        #     self.outputPdf('v-cut-map')
        #     if self.currentStep != self.vcutStep:
        #         self.GEN.CLOSE_STEP()
        # if self.GEN.LAYER_EXISTS('vcut') == 'yes':
        #     self.GEN.DELETE_LAYER('vcut')

    def selectTwoLine(self, outData):
        '''
        标注两根线间距
        :param outData:
        :return:
        '''
        status = True
        while status:
            self.GEN.FILTER_RESET()
            self.GEN.WORK_LAYER(self.outline)
            self.GEN.PAUSE('Please select two line...')
            if int(self.GEN.GET_SELECT_COUNT()) == 2:
                fPath = 'c:\\tmp\\twoline_point'
                self.GEN.COM(
                    'info, out_file={0}, units=mm,args= -t layer -e {1}/{2}/{3} -m display -d FEATURES -o select'.format(
                        fPath, self.JOB, self.mapStep, self.outline))
                with open(fPath, 'r') as f:
                    angleType = None
                    xs = None
                    ys = None
                    xe = None
                    ye = None
                    for value in f.readlines():
                        if re.search(re.compile('#L'), value):
                            info = value.split(' ')
                            if xs is None:
                                xs = float(info[1])
                                ys = float(info[2])
                                xe = float(info[3])
                                ye = float(info[4])
                            else:
                                if info[1] == info[3]:
                                    angleType = 'vertical'
                                    xs = xs
                                    ys = outData['ymin']
                                    xe = float(info[1])
                                    ye = outData['ymin']

                                elif info[2] == info[4]:
                                    angleType = 'horizontal'
                                    xs = outData['xmin']
                                    ys = ys
                                    xe = outData['xmin']
                                    ye = float(info[2])

                    baseSize1 = 0.2
                    baseSize2 = 2
                    baseSize3 = 3
                    width = round(abs(xs - xe), 2)
                    height = round(abs(ys - ye), 2)
                    if angleType == 'vertical':
                        if xs > xe:
                            xe, xs = xs, xe
                        # --下线长
                        xs1 = xs
                        xe1 = xe
                        ys1 = ye - baseSize2
                        ye1 = ye - baseSize2

                        # --下左线
                        xs2 = xs
                        xe2 = xs
                        ys2 = ye - baseSize1
                        ye2 = ye - baseSize3

                        # --下右线
                        xs3 = xe
                        xe3 = xe
                        ys3 = ye - baseSize1
                        ye3 = ye - baseSize3

                        textAngel = 0
                        textX = xs + (xe - xs) / 2 - len(str(height)) * 1.016 / 2
                        textY = ye - 4

                    else:
                        height, width = width, height
                        if ys > ye:
                            ye, ys = ys, ye
                        # --左线长
                        xs1 = xs - baseSize2
                        xe1 = xs - baseSize2
                        ys1 = ys
                        ye1 = ye

                        # --左下线
                        xs2 = xs - baseSize1
                        xe2 = xs - baseSize3
                        ys2 = ys
                        ye2 = ys

                        # --左上线
                        xs3 = xs - baseSize1
                        xe3 = xs - baseSize3
                        ys3 = ye
                        ye3 = ye

                        textAngel = 90
                        textX = xe - 4
                        textY = ys + (ye - ys) / 2 + len(str(width)) * 1.016 / 2

                    # --定义一个属性,方便清理旧资料
                    self.GEN.COM('cur_atr_set,attribute=.bit,text=map')

                    self.addLine(xs1, ys1, xe1, ye1, 'r100', attr='yes')
                    self.addLine(xs2, ys2, xe2, ye2, 'r100', attr='yes')
                    self.addLine(xs3, ys3, xe3, ye3, 'r100', attr='yes')

                    # --添加x方向尺寸
                    self.addText(textX, textY, width, angle=textAngel, attr='yes')

            elif int(self.GEN.GET_SELECT_COUNT()) > 0:
                self.message('warning', '系统提示', '请选择两根线,否则无法标注...')
            else:
                status = False

            if status is False:
                break

    def creHoleMap(self, layerName, step, boardThick, outData):
        '''
        创建分孔图
        :param layerName: 钻孔层
        :param step: step名
        :param boardThick:板厚
        :return:
        '''
        self.GEN.OPEN_STEP(step)
        self.GEN.FILTER_RESET()
        self.GEN.CLEAR_LAYER()
        mapLayer = 'map'
        if self.GEN.LAYER_EXISTS(mapLayer) == 'yes':
            self.GEN.DELETE_LAYER(mapLayer)
        self.GEN.COM(
            'cre_drills_map,layer={0},map_layer={1},preserve_attr=no,draw_origin=no,define_via_type=no,units=mm,mark_dim=1270,mark_line_width=101.6,sr=yes,slots=by_length,columns=Tool\;Count\;Finish\;Type,notype=plt,table_pos=right,table_align=bottom,sort_by=size,sort_dir=incr'.format(
                layerName, mapLayer))
        outLayer = 'out'
        if self.GEN.LAYER_EXISTS(outLayer) == 'yes':
            self.GEN.AFFECTED_LAYER(outLayer, 'yes')
            self.GEN.SEL_COPY(mapLayer)
            self.GEN.AFFECTED_LAYER(outLayer, 'no')
            self.GEN.AFFECTED_LAYER(mapLayer, 'yes')
            self.GEN.FILTER_TEXT_ATTR('.bit', 'map')
            self.GEN.FILTER_SELECT()
            if int(self.GEN.GET_SELECT_COUNT()) > 0:
                self.GEN.SEL_DELETE()
            self.createDrawing(outData, 1)
            tx = outData['xmin'] + 3
            ty = outData['ymax'] + 15
            # self.GEN.ADD_PAD(tx, ty, 'vcutlabel')
            self.addText(tx + 32, ty + 1, boardThick, x_size='3.81', y_size='5.08', w_factor='1.25', angle=0)
            self.GEN.AFFECTED_LAYER(mapLayer, 'no')

    def outputPdf(self, layerName):
        """
        输出PDF档操作
        :return:
        """
        # self.GEN.COM('print,title=,layer_name={0},mirrored_layers=,draw_profile=yes,drawing_per_layer=no,label_layers=no,dest=pdf_file,num_copies=1,dest_fname={1},paper_size=A4,scale_to=0,nx=1,ny=1,orient=none,paper_orient=portrait,paper_width=0,paper_height=0,auto_tray=no,top_margin=12.7,bottom_margin=12.7,left_margin=12.7,right_margin=12.7,x_spacing=10,y_spacing=10,color1=990000,color2=990000,color3=805000,color4=000099,color5=0,color6=0,color7=0'.format(layerName,os.path.join(self.outputPath, '%s.pdf' % self.JOB).replace('\\', '/')))
        self.GEN.COM(
            'print,title=,layer_name={0},mirrored_layers=,draw_profile=no,drawing_per_layer=yes,label_layers=no,dest=pdf_file,num_copies=1,dest_fname={1},paper_size=A4,scale_to=0,nx=1,ny=1,orient=none,paper_orient=portrait,paper_width=0,paper_height=0,auto_tray=no,top_margin=0,bottom_margin=0,left_margin=0,right_margin=0,x_spacing=0,y_spacing=0,color1=990000,color2=9900,color3=99,color4=990099,color5=999900,color6=9999,color7=0'.format(
                layerName, os.path.join(self.outputPath, '%s.pdf' % self.JOB).replace('\\', '/')))
        # --命令执行完成后，判断是否有PDF文档输出
        if not os.path.exists(os.path.join(self.outputPath, '%s.pdf' % self.JOB)):
            self.message('warning', '错误信息', '程序输出PDF档资料出错(可能原因gs插件或hooks下配置文件ps2pdf...)！')
            sys.exit(1)

    def createVcutMap(self, vcutData, vcutLayer='v-cut'):
        '''
        生成vcut图
        :param vcutData: vcut数据
        :param vcutLayer: vcut层
        :return:
        '''
        if len(vcutData.keys()) > 0:
            self.GEN.OPEN_STEP(self.vcutStep)
            self.GEN.CHANGE_UNITS('mm')
            self.GEN.FILTER_RESET()
            self.GEN.CLEAR_FEAT()
            self.GEN.CLEAR_LAYER()
            vcutBak = vcutLayer + '_bak'
            vcutMap = vcutLayer + '_map'
            self.GEN.COM('flatten_layer,source_layer={0},target_layer={1}'.format(vcutLayer, vcutBak))
            outData = self.getOutProfile(self.vcutStep)
            vcutDatap = self.getVcut(outData, self.vcutStep, vcut=vcutBak)
            if len(vcutDatap.keys()) > 0:
                self.GEN.COM('flatten_layer,source_layer={0},target_layer={1}'.format('gko', vcutMap))
                if self.GEN.LAYER_EXISTS(vcutMap) == 'no':
                    self.GEN.CREATE_LAYER(vcutMap)
                xstart = 0
                ystart = 0
                if self.GEN.LAYER_EXISTS('gts') == 'yes':
                    self.GEN.AFFECTED_LAYER('gts', 'yes')
                    self.GEN.FILTER_RESET()
                    self.GEN.FILTER_SET_INCLUDE_SYMS('r211')
                    self.GEN.FILTER_SELECT()
                    if int(self.GEN.GET_SELECT_COUNT()) > 0:
                        fPath = 'c:\\tmp\\pvcut_point'
                        self.GEN.COM(
                            'info, out_file={0}, units=mm,args= -t layer -e {1}/{2}/gts -m display -d FEATURES -o select'.format(
                                fPath, self.JOB, self.vcutStep))
                        with open(fPath, 'r') as f:
                            for line in f.readlines():
                                if '#P' in line:
                                    infoCoord = line.split(' ')
                                    xstart = round(float(infoCoord[1]), 2)
                                    ystart = round(float(infoCoord[2]), 2)

                self.GEN.FILTER_RESET()
                self.GEN.CLEAR_LAYER()
                self.GEN.AFFECTED_LAYER(vcutMap, 'yes')
                self.GEN.FILTER_TEXT_ATTR('.bit', 'map')
                self.GEN.FILTER_SELECT()
                if int(self.GEN.GET_SELECT_COUNT()) > 0:
                    self.GEN.SEL_DELETE()

                vcutNum = self.vcutNote(vcutDatap, xstart=xstart, ystart=ystart, step=self.vcutStep)
                self.GEN.ADD_PAD(xstart, ystart, 'r2200')
                tx = outData['xmin'] + 20
                ty = outData['ymax'] + 33
                # self.GEN.ADD_PAD(tx,ty,'lxdjjm21a', attr='yes')

                '''
                    基本参数
                    self.selAuthor = data['selAuthor']
                    self.residualThickness = data['residualThickness']
                    self.routTol = data['routTol']
                    self.vcutMode = data['vcutMode']
                    self.vcutAngle = data['vcutAngle']
                '''
                # -- add mode
                self.addText(tx, ty, self.vcutMode, x_size='2.5', y_size='2.5', w_factor='0.82020998',
                             fontname='simplex', angle=0, attr='yes')

                # -- add mode
                self.addText(tx, ty - 4.5, self.routTol, x_size='2.5', y_size='2.5', w_factor='0.82020998',
                             fontname='simplex', angle=0, attr='yes')

                # -- add selAuthor
                self.addText(tx, ty - 13.2, self.selAuthor, x_size='2.5', y_size='2.5', w_factor='0.82020998',
                             fontname='simplex', angle=0, attr='yes')

                # -- add residualThickness
                self.addText(tx + 41, ty - 12.6, self.residualThickness, x_size='2.5', y_size='2.5',
                             w_factor='0.82020998', fontname='simplex', angle=0, attr='yes')

                # -- add vcutAngle
                self.addText(tx + 60, ty + 4.2, self.vcutAngle, x_size='2.5', y_size='2.5', w_factor='0.82020998',
                             fontname='simplex', angle=0, attr='yes')

                # -- add boardThick
                self.addText(tx + 60, ty - 4.7, self.boardThick, x_size='2.5', y_size='2.5', w_factor='0.82020998',
                             fontname='simplex', angle=0, attr='yes')

                # -- add total vcut num
                self.addText(tx + 55, ty - 17.4, vcutNum, x_size='2.5', y_size='2.5', w_factor='0.82020998',
                             fontname='simplex', angle=0, attr='yes')

                self.GEN.AFFECTED_LAYER(vcutMap, 'no')
                if self.GEN.LAYER_EXISTS(vcutBak) == 'yes':
                    self.GEN.DELETE_LAYER(vcutBak)
                self.GEN.FILTER_RESET()
                self.GEN.CLEAR_LAYER()
            else:
                self.message('warning', '警告信息', '检测不到VCUT数据,请检查!(pnl)')
                sys.exit(0)
        else:
            self.message('warning', '警告信息', '检测不到VCUT数据,请检查!')
            sys.exit(0)

    def getEdirSr(self, outData):
        '''
        获取edit sr
        :param outData:
        :return:
        '''
        xmin = None
        ymin = None
        xmax = None
        ymax = None
        info = self.GEN.DO_INFO('-t step -e {0}/{1} -m script -d SR'.format(self.JOB, self.mapStep))
        for n in range(len(info['gSRstep'])):
            if re.search(re.compile('^edit'), info['gSRstep'][n]):
                if xmin is None:
                    xmin = float(info['gSRxmin'][n])
                    ymin = float(info['gSRymin'][n])
                    xmax = float(info['gSRxmax'][n])
                    ymax = float(info['gSRymax'][n])
                    if info['gSRnx'][n] != '1':
                        xmax = float(info['gSRxmax'][n]) - float(info['gSRdx'][n]) * (int(info['gSRnx'][n]) - 1)
                    if info['gSRny'][n] != '1':
                        ymax = float(info['gSRymax'][n]) - float(info['gSRdy'][n]) * (int(info['gSRny'][n]) - 1)
                else:
                    nxmin = xmin
                    nymin = ymin
                    nxmax = xmax
                    nymax = ymax
                    if info['gSRnx'][n] != '1':
                        nxmax = float(info['gSRxmax'][n]) - float(info['gSRdx'][n]) * (int(info['gSRnx'][n]) - 1)
                    if info['gSRny'][n] != '1':
                        nymax = float(info['gSRymax'][n]) - float(info['gSRdy'][n]) * (int(info['gSRny'][n]) - 1)

                    if nxmin < xmin or nymin < ymin or nxmax < xmax or nymax < ymax:
                        xmin = nxmin
                        ymin = nymin
                        xmax = nxmax
                        ymax = nymax
        return {
            'xmin': xmin,
            'ymin': ymin,
            'xmax': xmax,
            'ymax': ymax
        }

    def otherNote(self, outData, editSr, vcutData=None):
        '''
        标注其他数据
        :param outData: 外形数据
        :param vcutData: vcut数据
        :param editSr: 单元尺寸
        :return:
        '''
        """
        outData = {
            'xmin': xmin,
            'ymin': ymin,
            'xmax': xmax,
            'ymax': ymax,
            'gSRxmin': gSRxmin,
            'gSRymin': gSRymin,
            'gSRxmax': gSRxmax,
            'gSRymax': gSRymax,
            'nxmin': nxmin,
            'nymin': nymin,
            'nxmax': nxmax,
            'nymax': nymax,
        }

        vcutData[str(n)] = {
            'xs':xs,
            'ys':ys,
            'xe':xe,
            'ye':ye,
            'type':angleType
        }
        """

        self.GEN.FILTER_RESET()
        self.GEN.CLEAR_FEAT()
        self.GEN.CLEAR_LAYER()
        self.GEN.AFFECTED_LAYER(self.outline, 'yes')
        if self.mapStep != 'edit':
            self.createDrawing(outData, 1)
        if vcutData is not None:
            vcutNum = self.vcutNote(vcutData)
        # --当前step不等于edit,直接跳过不标注单元尺寸 AresHe 2023.8.25
        # if self.mapStep != 'edit':
        self.editNote(outData, editSr)
        self.setNote(outData)
        # tx = outData['xmin'] + 20
        # ty = outData['ymax'] + 33

        # self.GEN.FILTER_TEXT_ATTR('.bit', 'map')
        # # self.GEN.ADD_PAD(tx, ty, 'lxdjjm21a', attr='yes')
        # # -- add mode
        # self.addText(tx, ty, self.vcutMode, x_size='2.5', y_size='2.5', w_factor='0.82020998', fontname='simplex',angle=0, attr='yes')
        #
        # # -- add mode
        # self.addText(tx, ty - 4.5, self.routTol, x_size='2.5', y_size='2.5', w_factor='0.82020998', fontname='simplex',angle=0, attr='yes')
        #
        # # -- add selAuthor
        # self.addText(tx, ty - 13.2, self.selAuthor, x_size='2.5', y_size='2.5', w_factor='0.82020998',fontname='simplex', angle=0, attr='yes')
        #
        # # -- add residualThickness
        # self.addText(tx + 41, ty - 12.6, self.residualThickness, x_size='2.5', y_size='2.5', w_factor='0.82020998',fontname='simplex', angle=0, attr='yes')
        #
        # # -- add vcutAngle
        # self.addText(tx + 60, ty + 4.2, self.vcutAngle, x_size='2.5', y_size='2.5', w_factor='0.82020998',fontname='simplex', angle=0, attr='yes')
        #
        # # -- add boardThick
        # self.addText(tx + 60, ty - 4.7, self.boardThick, x_size='2.5', y_size='2.5', w_factor='0.82020998',fontname='simplex', angle=0, attr='yes')

        # self.GEN.ADD_PAD(tx, ty, 'vcutlabel')
        # self.addText(tx + 32, ty + 1, self.boardThick, x_size='3.81', y_size='5.08', w_factor='1.25', angle=0)
        self.GEN.FILTER_RESET()
        self.GEN.CLEAR_FEAT()
        self.GEN.CLEAR_LAYER()
        self.GEN.AFFECTED_LAYER(self.outline, 'no')

    def setNote(self, outData):
        '''
        outData
        {
            'xmin': limitsXmin,
            'ymin': limitsYmin,
            'xmax': limitsXmax,
            'ymax': limitsYmax,
            'xCenter': xCenter,
            'yCemter': yCenter,
            'nxmin': nxmin,
            'nymin': nymin,
            'nxmax': nxmax,
            'nymax': nymax,
        }
        '''
        if abs(outData['xmin'] - outData['nxmin']) > 1:
            height = round(outData['nxmin'] - outData['xmin'], 2)
            # dl
            xs4 = outData['xmin']
            xe4 = outData['xmin']
            ys4 = outData['ymin']
            ye4 = outData['ymin'] - 3

            # dr
            xs5 = outData['nxmin']
            xe5 = outData['nxmin']
            ys5 = outData['ymin']
            ye5 = outData['ymin'] - 3

            # d length
            xs6 = outData['xmin']
            xe6 = outData['nxmin']
            ys6 = outData['ymin'] - 2.5
            ye6 = outData['ymin'] - 2.5

            self.addLine(xs4, ys4, xe4, ye4, 'r50', attr='yes')
            self.addLine(xs5, ys5, xe5, ye5, 'r50', attr='yes')
            self.addLine(xs6, ys6, xe6, ye6, 'r50', attr='yes')

            self.addPad(xs6 + 0.25, ys6, 'tri300x500', angle=270, attr='yes')
            self.addPad(xe6 - 0.25, ys6, 'tri300x500', angle=90, attr='yes')

            textX2 = outData['xmin'] + (outData['nxmin'] - outData['xmin']) / 2 - len(str(height)) * 1.016 / 2
            textY2 = outData['ymin'] - 4.5 - 1.5
            textAngel2 = 0

            # --添加y方向尺寸
            self.addText(textX2, textY2, height, x_size='2.032', y_size='3.048', angle=textAngel2, attr='yes')

        if abs(outData['xmax'] - outData['nxmax']) > 1:
            width = round(outData['nymax'] - outData['nymax'], 2)
            height = round(outData['xmax'] - outData['nxmax'], 2)
            # dl
            xs4 = outData['nxmax']
            xe4 = outData['nxmax']
            ys4 = outData['ymin']
            ye4 = outData['ymin'] - 3

            # dr
            xs5 = outData['xmax']
            xe5 = outData['xmax']
            ys5 = outData['ymin']
            ye5 = outData['ymin'] - 3

            # d length
            xs6 = outData['nxmax']
            xe6 = outData['xmax']
            ys6 = outData['ymin'] - 2.5
            ye6 = outData['ymin'] - 2.5

            self.addLine(xs4, ys4, xe4, ye4, 'r50', attr='yes')
            self.addLine(xs5, ys5, xe5, ye5, 'r50', attr='yes')
            self.addLine(xs6, ys6, xe6, ye6, 'r50', attr='yes')

            self.addPad(xs6 + 0.25, ys6, 'tri300x500', angle=270, attr='yes')
            self.addPad(xe6 - 0.25, ys6, 'tri300x500', angle=90, attr='yes')

            textX2 = outData['nxmax'] + (outData['xmax'] - outData['nxmax']) / 2 - len(str(height)) * 1.016 / 2
            textY2 = outData['ymin'] - 4.5 - 1.5
            textAngel2 = 0

            # --添加y方向尺寸
            self.addText(textX2, textY2, height, x_size='2.032', y_size='3.048', angle=textAngel2, attr='yes')

        if abs(outData['ymin'] - outData['nymin']) > 1:
            width = round(outData['nymin'] - outData['ymin'], 2)

            # lup
            xs1 = outData['xmin'] - 3
            xe1 = outData['nxmin']
            ys1 = outData['nymin']
            ye1 = outData['nymin']

            # ldown
            xs2 = outData['xmin'] - 3
            xe2 = outData['nxmin']
            ys2 = outData['ymin']
            ye2 = outData['ymin']

            # l length
            xs3 = outData['xmin'] - 2.5
            xe3 = outData['xmin'] - 2.5
            ys3 = outData['ymin']
            ye3 = outData['nymin']

            self.addLine(xs1, ys1, xe1, ye1, 'r50', attr='yes')
            self.addLine(xs2, ys2, xe2, ye2, 'r50', attr='yes')
            self.addLine(xs3, ys3, xe3, ye3, 'r50', attr='yes')

            # tri300x500
            self.addPad(xs3, ye3 - 0.25, 'tri300x500', angle=0, attr='yes')
            self.addPad(xs3, ys3 + 0.25, 'tri300x500', angle=180, attr='yes')

            textX1 = outData['xmin'] - 4.5 - 1.5
            textY1 = outData['ymin'] + (outData['nymin'] - outData['ymin']) / 2 + len(str(width)) * 1.016 / 2
            textAngel1 = 90

            # --添加x方向尺寸
            self.addText(textX1, textY1, width, x_size='2.032', y_size='3.048', angle=textAngel1, attr='yes')

        if abs(outData['ymax'] - outData['nymax']) > 1:
            width = round(outData['ymax'] - outData['nymax'], 2)
            # lup
            xs1 = outData['xmin'] - 3
            xe1 = outData['nxmin']
            ys1 = outData['nymax']
            ye1 = outData['nymax']

            # ldown
            xs2 = outData['xmin'] - 3
            xe2 = outData['nxmin']
            ys2 = outData['ymax']
            ye2 = outData['ymax']

            # l length
            xs3 = outData['xmin'] - 2.5
            xe3 = outData['xmin'] - 2.5
            ys3 = outData['ymax']
            ye3 = outData['nymax']

            self.addLine(xs1, ys1, xe1, ye1, 'r50', attr='yes')
            self.addLine(xs2, ys2, xe2, ye2, 'r50', attr='yes')
            self.addLine(xs3, ys3, xe3, ye3, 'r50', attr='yes')

            # tri300x500
            self.addPad(xs3, ye3 - 0.25, 'tri300x500', angle=0, attr='yes')
            self.addPad(xs3, ys3 + 0.25, 'tri300x500', angle=180, attr='yes')

            textX1 = outData['xmin'] - 4.5 - 1.5
            textY1 = outData['nymax'] + (outData['ymax'] - outData['nymax']) / 2 + len(str(width)) * 1.016 / 2
            textAngel1 = 90

            # --添加x方向尺寸
            self.addText(textX1, textY1, width, x_size='2.032', y_size='3.048', angle=textAngel1, attr='yes')

    def editNote(self, outData, editSr):
        '''
        标注单元尺寸
        :param outData: 外形数据
        :param editSr:  单元数据
        :return:
        '''
        if editSr['xmin'] is not None:
            width = round(editSr['ymax'] - editSr['ymin'], 2)
            height = round(editSr['xmax'] - editSr['xmin'], 2)

            # lup
            xs1 = outData['xmin'] - 3
            xe1 = editSr['xmin']
            ys1 = editSr['ymax']
            ye1 = editSr['ymax']

            # ldown
            xs2 = outData['xmin'] - 3
            xe2 = editSr['xmin']
            ys2 = editSr['ymin']
            ye2 = editSr['ymin']

            # l length
            xs3 = outData['xmin'] - 2.5
            xe3 = outData['xmin'] - 2.5
            ys3 = editSr['ymin']
            ye3 = editSr['ymax']

            # ul
            xs4 = editSr['xmin']
            xe4 = editSr['xmin']
            ys4 = editSr['ymin']
            ye4 = outData['ymin'] - 3

            # ur
            xs5 = editSr['xmax']
            xe5 = editSr['xmax']
            ys5 = editSr['ymin']
            ye5 = outData['ymin'] - 3

            # u length
            xs6 = editSr['xmin']
            xe6 = editSr['xmax']
            ys6 = outData['ymin'] - 2.5
            ye6 = outData['ymin'] - 2.5

            self.addLine(xs1, ys1, xe1, ye1, 'r50', attr='yes')
            self.addLine(xs2, ys2, xe2, ye2, 'r50', attr='yes')
            self.addLine(xs3, ys3, xe3, ye3, 'r50', attr='yes')
            self.addLine(xs4, ys4, xe4, ye4, 'r50', attr='yes')
            self.addLine(xs5, ys5, xe5, ye5, 'r50', attr='yes')
            self.addLine(xs6, ys6, xe6, ye6, 'r50', attr='yes')

            # tri300x500
            self.addPad(xs3, ye3 - 0.25, 'tri300x500', angle=0, attr='yes')
            self.addPad(xs3, ys3 + 0.25, 'tri300x500', angle=180, attr='yes')

            self.addPad(xs6 + 0.25, ys6, 'tri300x500', angle=270, attr='yes')
            self.addPad(xe6 - 0.25, ys6, 'tri300x500', angle=90, attr='yes')

            textX1 = outData['xmin'] - 5 - 1.5
            textY1 = editSr['ymin'] + (editSr['ymax'] - editSr['ymin']) / 2 + len(str(width)) * 1.016 / 2
            textAngel1 = 90

            textX2 = editSr['xmin'] + (editSr['xmax'] - editSr['xmin']) / 2 - len(str(height)) * 1.016 / 2
            textY2 = outData['ymin'] - 4.5 - 1.5
            textAngel2 = 0

            # --添加x方向尺寸
            self.addText(textX1, textY1, width, x_size='2.032', y_size='3.048', angle=textAngel1, attr='yes')

            # --添加y方向尺寸
            self.addText(textX2, textY2, height, x_size='2.032', y_size='3.048', angle=textAngel2, attr='yes')

    def analyseOut(self, filePath='c:/tmp/features__info'):
        '''
        分析out数据
        :return:
        '''

        bakLayer = self.outline + '_bak'
        bakLayer2 = self.outline + '_bak2'
        bakLayer3 = self.outline + '_bak3'
        if self.GEN.LAYER_EXISTS(bakLayer) == 'yes':
            self.GEN.DELETE_LAYER(bakLayer)
        self.GEN.SEL_COPY(bakLayer)
        self.GEN.CLEAR_LAYER()
        self.GEN.AFFECTED_LAYER(bakLayer, 'yes')
        self.GEN.SEL_COPY(bakLayer2)
        self.GEN.CLEAR_LAYER()
        self.GEN.AFFECTED_LAYER(bakLayer2, 'yes')
        self.GEN.COM(
            'sel_cut_data,det_tol=25.4,con_tol=25.4,rad_tol=2.54,filter_overlaps=no,delete_doubles=no,use_order=yes,ignore_width=yes,ignore_holes=none,start_positive=yes,polarity_of_touching=same')
        self.GEN.SEL_RESIZE('200')
        if self.GEN.LAYER_EXISTS(bakLayer2 + '+++') == 'yes':
            self.GEN.DELETE_LAYER(bakLayer2 + '+++')
        self.GEN.FILTER_SET_FEAT_TYPES('surface')
        self.GEN.FILTER_SELECT()
        count = int(self.GEN.GET_SELECT_COUNT())
        if count > 0:
            self.GEN.SEL_MOVE(bakLayer3)

        self.GEN.AFFECTED_LAYER(bakLayer2, 'no')
        self.GEN.AFFECTED_LAYER(bakLayer, 'yes')
        self.GEN.COM('sel_change_sym,symbol=r1,reset_angle=no')
        self.GEN.AFFECTED_LAYER(bakLayer, 'no')

        data = dict()
        self.GEN.AFFECTED_LAYER(bakLayer3, 'yes')
        for n in range(count):
            m = n + 1
            self.GEN.COM('sel_layer_feat,operation=select,layer={},index={}'.format(bakLayer3, m))
            if int(self.GEN.GET_SELECT_COUNT()) > 0:
                self.GEN.AFFECTED_LAYER(bakLayer, 'yes')
                self.GEN.FILTER_RESET()
                self.GEN.COM(
                    'sel_ref_feat,layers=,use=select,mode=touch,pads_as=shape,f_types=line\;pad\;surface\;arc\;text,polarity=positive\;negative,include_syms=,exclude_syms=')
                if int(self.GEN.GET_SELECT_COUNT()) > 0:
                    limitsInfo = self.GEN.DO_INFO(
                        '-t layer -e {0}/{1}/{2} -m script -d LIMITS -o select'.format(self.JOB, self.mapStep,
                                                                                       bakLayer))
                    self.GEN.COM(
                        'info, out_file={0}, units=mm,args=  -t layer -e {1}/{2}/{3} -m script -d FEATURES -o select'.format(
                            filePath, self.JOB, self.mapStep, bakLayer))
                    xCenter = float(limitsInfo['gLIMITSxcenter'])
                    yCenter = float(limitsInfo['gLIMITSycenter'])
                    angle = None
                    with open(filePath, 'r') as f:
                        index = 0
                        for line in f.readlines():
                            if '#L' in line:
                                index = index + 1
                                info = line.split(' ')
                                xs = float(info[1])
                                ys = float(info[2])
                                xe = float(info[3])
                                ye = float(info[4])
                                fType = 'line'
                            elif '#A' in line:
                                index = index + 1
                                info = line.split(' ')
                                xs = float(info[1])
                                ys = float(info[2])
                                xe = float(info[3])
                                ye = float(info[4])
                                fType = 'arc'
                            else:
                                continue
                            if angle is None and fType == 'line':
                                # --判断线是在中心左边的线
                                if xs != xe and ys != ye:
                                    x = abs(xe - xs)
                                    y = abs(ye - ys)
                                    xCoord = abs(xs - xe) / 2
                                    yCoord = abs(ys - ye) / 2
                                    if xs < xe:
                                        xCoord = xs + xCoord
                                    else:
                                        xCoord = xe + xCoord
                                    if ys < ye:
                                        yCoord = ys + yCoord
                                    else:
                                        yCoord = ye + yCoord
                                    if xCoord < xCenter:
                                        if yCoord > yCenter:
                                            # --lUp
                                            # print ("lUp")
                                            angle = round(self.getAngle(y, x), 2)
                                        else:
                                            # --lDown
                                            # print("lDown")
                                            angle = round(self.getAngle(x, y), 2)
                                    else:
                                        if yCoord > yCenter:
                                            # --rUp
                                            # print("rUp")
                                            angle = round(self.getAngle(x, y), 2)
                                        else:
                                            # --rDown
                                            # print("rDown")
                                            angle = round(self.getAngle(y, x), 2)
                                    # print ('xs:'+str(xs))
                                    # print ('ys:'+str(ys))
                                    # print ('xe:'+str(xe))
                                    # print ('ye:'+str(ye))
                                    # print ('xCenter:'+str(xCenter))
                                    # print ('yCenter:'+str(yCenter))
                                    # print (angle)
                                    # sys.exit(0)
                                else:
                                    x = abs(xe - xs)
                                    y = abs(ye - ys)
                                    angle = round(self.getAngle(x, y), 2)
                                    print(type(angle))
                    if angle is not None:
                        bakLayerTmp = bakLayer + '_' + str(n) + '_' + str(angle)
                        data[str(n)] = {
                            'layerName': bakLayerTmp,
                            'angle': angle,
                            'xCenter': xCenter,
                            'yCenter': yCenter,
                            'index': n
                        }
                        if self.GEN.LAYER_EXISTS(bakLayerTmp) == 'yes':
                            self.GEN.DELETE_LAYER(bakLayerTmp)
                        self.GEN.SEL_MOVE(bakLayerTmp)
                    '''
                    所有外形,必须得保证连接正确(不允许有多段不规则的连接方式,比如圆弧位置存在line相连,则会影响到系统判断角度)  AresHe 2023.8.12
                    '''
                self.GEN.CLEAR_FEAT()
                self.GEN.AFFECTED_LAYER(bakLayer, 'no')
        self.GEN.FILTER_RESET()
        self.GEN.CLEAR_LAYER()
        self.GEN.CLEAR_FEAT()
        self.disposeDrawing(data)

        for bk in [bakLayer, bakLayer2, bakLayer3]:
            if self.GEN.LAYER_EXISTS(bk):
                self.GEN.DELETE_LAYER(bk)

    def disposeDrawing(self, data=None):
        '''
        生成数据
        :param data:筛选后物件数据
        :return:
        '''

        """
        data[str(n)] = {
            'layerName':bakLayerTmp,
            'angle':angle,
            'xCenter':xCenter,
            'yCenter':yCenter,
            'index':n
        }
        """

        if data is not None:
            # --控制台提示信息
            print('\n###########*****Starting dispose the drawing!*****############\n')
            for n, k in enumerate(data.keys()):
                # --控制台提示信息,index No.(n)
                print('\n########  No.{0}  ########\n'.format(data[k]['index']))
                self.GEN.AFFECTED_LAYER(data[k]['layerName'], 'yes')
                # --不在范围内将不旋转。
                if data[k]['angle'] != 0 and data[k]['angle'] != 90 and data[k]['angle'] != 180 and data[k][
                    'angle'] != 270:
                    # --旋转角度
                    self.rotateAngle(data[k]['xCenter'], data[k]['yCenter'], data[k]['angle'])
                # --获取物件信息
                fLimits = self.getFeaturesInfo(data[k]['layerName'])
                self.createDrawing(fLimits)

                # --不在范围内将不旋转。
                if data[k]['angle'] != 0 and data[k]['angle'] != 90 and data[k]['angle'] != 180 and data[k][
                    'angle'] != 270:

                    '''
                    genesis 9.7版本text不支持非常规0、90、180、270角度旋转(10.3版本正常,其他版本待测试)  AresHe 2023.8.12
                    '''
                    if re.search('9.7', self.GEN.GET_VERSION()):
                        self.GEN.SEL_BREAK()

                    # --旋转角度
                    self.rotateAngle(data[k]['xCenter'], data[k]['yCenter'], data[k]['angle'], 1)
                self.moveNote()
                self.GEN.AFFECTED_LAYER(data[k]['layerName'], 'no')
                if self.GEN.LAYER_EXISTS(data[k]['layerName']) == 'yes':
                    self.GEN.DELETE_LAYER(data[k]['layerName'])
        else:
            self.message('warning', '警告信息', '解析不到物件坐标信息,程序退出!')

    def moveNote(self):
        '''
        将标记移到外形层
        :return:
        '''
        self.GEN.FILTER_RESET()
        self.GEN.FILTER_TEXT_ATTR('.bit', 'map')
        self.GEN.FILTER_SELECT()
        if int(self.GEN.GET_SELECT_COUNT()) > 0:
            self.GEN.SEL_MOVE(self.outline)
        self.GEN.FILTER_RESET()

    def vcutNote(self, data, xstart=None, ystart=None, step=None):
        '''
        标注单元内vcut信息
        :param data:vcut数据
        :return:
        '''

        """
        vcutData[str(n)] = {
            'xs':xs,
            'ys':ys,
            'xe':xe,
            'ye':ye,
            'type':vertical/horizontal
        }
        """
        vList = []
        hList = []
        for k in data.keys():
            # print (data[k])
            if data[k]['type'] == 'vertical':
                # --竖方向
                xs = xe = data[k]['xs']
                ys = data[k]['ys']
                ye = data[k]['ys'] - 3
                self.addLine(xs, ys, xe, ye, 'r100', attr='yes')
                vList.append(round(xs, 2))
                content = round(data[k]['xmin'] + data[k]['xs'], 2)
                if step is not None:
                    content = round(content - xstart, 2)
                # --按一个字符长度计算
                tx = xs - 1 * 3.5 / 2
                ty = ye - 1
                ta = 90
                self.addText(tx, ty, content, x_size='3.5', y_size='3.5', w_factor='1.14', angle=ta, attr='yes')
            else:
                # --横方向
                ys = ye = data[k]['ys']
                xs = data[k]['xe']
                xe = data[k]['xe'] + 3
                self.addLine(xs, ys, xe, ye, 'r100', attr='yes')
                hList.append(round(ys, 2))
                content = round(data[k]['ymin'] + data[k]['ys'], 2)
                if step is not None:
                    content = round(content - ystart, 2)
                tx = xe + 1
                # --按一个字符长度计算
                ty = ys - 1 * 3.5 / 2
                ta = 0
                self.addText(tx, ty, content, x_size='3.5', y_size='3.5', w_factor='1.14', angle=ta, attr='yes')
        return int((len(set(vList)) + len(set(hList))))

    def createDrawing(self, data, dataType=None):
        '''
        生成坐标数据
        :param data:数据
        :return:
        '''

        """
        {
            'xmin':limitsXmin,
            'ymin':limitsYmin,
            'xmax':limitsXmax,
            'ymax':limitsYmax,
            'xCenter':xCenter,
            'yCemter':yCenter,
        }
        """

        width = round((data['ymax'] - data['ymin']), 2)
        height = round((data['xmax'] - data['xmin']), 2)

        baseSize1 = 0.2
        baseSize2 = 2
        baseSize3 = 3
        if dataType is not None:
            baseSize1 = 0
            baseSize2 = 6
            baseSize3 = 7

        # --左线长
        xs1 = data['xmin'] - baseSize2
        xe1 = data['xmin'] - baseSize2
        ys1 = data['ymin']
        ye1 = data['ymax']

        # --左下线
        xs2 = data['xmin'] - baseSize1
        xe2 = data['xmin'] - baseSize3
        ys2 = data['ymin']
        ye2 = data['ymin']

        # --左上线
        xs3 = data['xmin'] - baseSize1
        xe3 = data['xmin'] - baseSize3
        ys3 = data['ymax']
        ye3 = data['ymax']

        # --上线长
        xs4 = data['xmin']
        xe4 = data['xmax']
        ys4 = data['ymax'] + baseSize2
        ye4 = data['ymax'] + baseSize2

        # --上左线
        xs5 = data['xmin']
        xe5 = data['xmin']
        ys5 = data['ymax'] + baseSize1
        ye5 = data['ymax'] + baseSize3

        # --上右线
        xs6 = data['xmax']
        xe6 = data['xmax']
        ys6 = data['ymax'] + baseSize1
        ye6 = data['ymax'] + baseSize3

        # --定义一个属性,方便清理旧资料
        self.GEN.COM('cur_atr_set,attribute=.bit,text=map')

        self.addLine(xs1, ys1, xe1, ye1, 'r50', attr='yes')
        self.addLine(xs2, ys2, xe2, ye2, 'r50', attr='yes')
        self.addLine(xs3, ys3, xe3, ye3, 'r50', attr='yes')
        self.addLine(xs4, ys4, xe4, ye4, 'r50', attr='yes')
        self.addLine(xs5, ys5, xe5, ye5, 'r50', attr='yes')
        self.addLine(xs6, ys6, xe6, ye6, 'r50', attr='yes')

        # tri300x500
        self.addPad(xs1, ye1 - 0.25, 'tri300x500', angle=0, attr='yes')
        self.addPad(xs1, ys1 + 0.25, 'tri300x500', angle=180, attr='yes')

        self.addPad(xs4 + 0.25, ys4, 'tri300x500', angle=270, attr='yes')
        self.addPad(xe4 - 0.25, ys4, 'tri300x500', angle=90, attr='yes')

        textX1 = data['xmin'] - 4
        textY1 = data['ymin'] + (data['ymax'] - data['ymin']) / 2 + len(str(width)) * 1.016 / 2
        textAngel1 = 90

        textX2 = data['xmin'] + (data['xmax'] - data['xmin']) / 2 - len(str(height)) * 1.016 / 2
        textY2 = data['ymax'] + 2.5
        textAngel2 = 0

        if dataType is not None:
            textX1 = data['xmin'] - 10
            textY2 = data['ymax'] + 8.5

        # --添加x方向尺寸
        self.addText(textX1, textY1, width, x_size='2.032', y_size='3.048', angle=textAngel1, attr='yes')

        # --添加y方向尺寸
        self.addText(textX2, textY2, height, x_size='2.032', y_size='3.048', angle=textAngel2, attr='yes')

    def addPad(self, x, y, symbol, polarity='positive', angle=0, mirror='no', nx=1, ny=1, dx=0, dy=0, xscale=1,
               yscale=1, attr='no'):
        '''
        添加PAD
        :param x: x坐标
        :param y: y坐标
        :param symbol: symbol名
        :param polarity: 极性
        :param angle: 角度
        :param mirror: 镜像
        :param nx: x个数
        :param ny: y个数
        :param dx: x方向间距
        :param dy: y方向间距
        :param xscale: x比例
        :param yscale: y比例
        :return:
        '''
        self.GEN.COM(
            'add_pad,attributes={12},x={0},y={1},symbol={2},polarity={3},angle={4},mirror={5},nx={6},ny={7},dx={8},dy={9},xscale={10},yscale={11}'.format(
                x, y, symbol, polarity, angle, mirror, nx, ny, dx, dy, xscale, yscale, attr))

    def addLine(self, xs, ys, xe, ye, sym, polarity='positive', attr='no'):
        '''
        添加线
        :param xs:开始x
        :param ys:开始y
        :param xe:结束x
        :param ye:结束y
        :param sym:symbol大小
        :param polarity:极性
        :return:
        '''
        self.GEN.COM(
            'add_line,attributes={6},xs={0},ys={1},xe={2},ye={3},symbol={4},polarity={5},bus_num_lines=0,bus_dist_by=pitch,bus_distance=0,bus_reference=left'.format(
                xs, ys, xe, ye, sym, polarity, attr))

    def addText(self, x, y, text, x_size='1.016', y_size='1.524', w_factor='0.5', polarity='positive', angle=90,
                mirror='no', fontname='simple', attr='no'):
        '''
        添加字符
        :param x:x坐标
        :param y:y坐标
        :param text:内容
        :param x_size:宽度
        :param y_size:高度
        :param w_factor:
        :param polarity:极性
        :param angle:角度
        :param mirror:yes/no
        :param fontname:字体格式
        :return:
        '''
        self.GEN.COM(
            'add_text,attributes={10},type=string,x={0},y={1},text={2},x_size={3},y_size={4},w_factor={5},polarity={6},angle={7},mirror={8},fontname={9},ver=0'.format(
                x, y, text, x_size, y_size, w_factor, polarity, angle, mirror, fontname, attr))

    def rotateAngle(self, xCenter, yCenter, angle, restore=None):
        '''
        旋转角度
        :param angle:角度
        :param xCenter: x中心
        :param yCenter: y中心
        :return:
        '''
        if restore is None:
            angle = 360 - angle
        self.GEN.COM(
            'sel_transform,mode=anchor,oper=rotate,duplicate=no,x_anchor={0},y_anchor={1},angle={2},x_scale=1,y_scale=1,x_offset=0,y_offset=0'.format(
                xCenter, yCenter, angle))

    def getFeaturesInfo(self, layerName):
        '''
        获取物件信息
        :param layerName:层名
        :return: 返回中心,以边缘坐标
        '''

        info = self.GEN.DO_INFO('-t layer -e {0}/{1}/{2} -m script -d LIMITS'.format(self.JOB, self.mapStep, layerName))
        limitsXmin = float(info['gLIMITSxmin'])
        limitsYmin = float(info['gLIMITSymin'])
        limitsXmax = float(info['gLIMITSxmax'])
        limitsYmax = float(info['gLIMITSymax'])
        xCenter = float(info['gLIMITSxcenter'])
        yCenter = float(info['gLIMITSycenter'])

        return {
            'xmin': limitsXmin,
            'ymin': limitsYmin,
            'xmax': limitsXmax,
            'ymax': limitsYmax,
            'xCenter': xCenter,
            'yCemter': yCenter,
        }

    def getOutProfile(self, step):
        '''
        获取外形、单元尺寸坐标
        :return:
        '''
        info = self.GEN.DO_INFO('-t step -e {0}/{1} -m script -d PROF_LIMITS'.format(self.JOB, step))
        xmin = float(info['gPROF_LIMITSxmin'])
        ymin = float(info['gPROF_LIMITSymin'])
        xmax = float(info['gPROF_LIMITSxmax'])
        ymax = float(info['gPROF_LIMITSymax'])

        infosr = self.GEN.DO_INFO('-t step -e {0}/{1} -m script -d SR_LIMITS'.format(self.JOB, step))
        nxmin = float(infosr['gSR_LIMITSxmin'])
        nymin = float(infosr['gSR_LIMITSymin'])
        nxmax = float(infosr['gSR_LIMITSxmax'])
        nymax = float(infosr['gSR_LIMITSymax'])

        gSRxmin = None
        gSRymin = None
        gSRxmax = None
        gSRymax = None
        srInfo = self.GEN.DO_INFO('-t step -e {0}/{1} -m script -d SR'.format(self.JOB, step))
        for n, step in enumerate(srInfo['gSRstep']):
            if gSRxmin is None and re.search(re.compile('edit'), step):
                gSRxmin = float(srInfo['gSRxmin'][n])
                gSRymin = float(srInfo['gSRymin'][n])
                gSRxmax = float(srInfo['gSRxmax'][n])
                gSRymax = float(srInfo['gSRymax'][n])
            if re.search(re.compile('edit'), step):
                if gSRxmin < float(srInfo['gSRxmin'][n]):
                    gSRxmin = float(srInfo['gSRxmin'][n])
                if gSRymin < float(srInfo['gSRymin'][n]):
                    gSRymin = float(srInfo['gSRymin'][n])
                if gSRxmax < float(srInfo['gSRxmax'][n]):
                    gSRxmax = float(srInfo['gSRxmax'][n])
                if gSRymax < float(srInfo['gSRymax'][n]):
                    gSRymax = float(srInfo['gSRymax'][n])

        data = {
            'xmin': xmin,
            'ymin': ymin,
            'xmax': xmax,
            'ymax': ymax,
            'gSRxmin': gSRxmin,
            'gSRymin': gSRymin,
            'gSRxmax': gSRxmax,
            'gSRymax': gSRymax,
            'nxmin': nxmin,
            'nymin': nymin,
            'nxmax': nxmax,
            'nymax': nymax,
        }
        return data

    def getVcut(self, outData, step, vcut='vcut', tmpFile='c:\\tmp\\vcut_line'):
        '''
        获取vcut线坐标
        :param outData:
        :param step:
        :param vcut:
        :param tmpFile:
        :return:
        '''
        return None
        if self.GEN.LAYER_EXISTS(vcut) == 'yes':
            self.GEN.AFFECTED_LAYER(vcut, 'yes')
            # --去重线
            self.GEN.COM('sel_design2rout,det_tol=25.4,con_tol=25.4,rad_tol=2.54')
            self.GEN.AFFECTED_LAYER(vcut, 'no')
            self.GEN.COM(
                'info, out_file={0},units=mm,args=  -t layer -e {1}/{2}/{3} -m script -d FEATURES'.format(tmpFile,
                                                                                                          self.JOB,
                                                                                                          step, vcut))
            data = dict()
            with open(tmpFile, 'r') as f:
                for n, value in enumerate(f.readlines()):
                    if re.search(re.compile('#L'), value):
                        info = value.split(' ')
                        xs = float(info[1])
                        ys = float(info[2])
                        xe = float(info[3])
                        ye = float(info[4])
                        if info[1] == info[3]:
                            angleType = 'vertical'
                            ys = outData['ymin']
                            ye = outData['ymax']
                        elif info[2] == info[4]:
                            angleType = 'horizontal'
                            xs = outData['xmin']
                            xe = outData['xmax']
                        else:
                            angleType = None
                        data[str(n)] = {
                            'xs': xs,
                            'ys': ys,
                            'xe': xe,
                            'ye': ye,
                            'type': angleType,
                            'xmin': outData['xmin'],
                            'xmax': outData['xmax'],
                            'ymin': outData['ymin'],
                            'ymax': outData['ymax']
                        }
            return data

    def getAngle(self, width, height):
        '''
        三角函数:sinA = 对边 / 邻边
        :param width: 对边
        :param height: 邻边
        :return:
        '''

        x = width
        y = height

        # if x > y:
        y, x = x, y
        result = math.atan2(x, y) * 180 / math.pi
        return result

    def message(self, messageType, messageTitle, messageContent):
        '''
        message提示信息
        :param messageType: 提示类型
        :param messageTitle: 提示抬头
        :param messageContent: 提示内容
        :return:
        '''

        if messageType == 'info':
            msg_box = QMessageBox(QMessageBox.Information, messageTitle, messageContent)
            msg_box.exec_()
        elif messageType == 'warning':
            msg_box = QMessageBox(QMessageBox.Warning, messageTitle, messageContent)
            msg_box.exec_()


if __name__ == '__main__':
    '''
    1.只有直接运行本程序才会进入这个程序接口
    2.假如其他脚本调用本程序文件，不会进入这里
    '''
    app = QtWidgets.QApplication(sys.argv)
    m = MAIN()
    m.setWindows()
    sys.exit(app.exec_())
