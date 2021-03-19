# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 12:06:09 2021

@author: shane
"""

from src.seltools import main
from src.HCM_main import hcm
from time import sleep

   
class pospages(hcm,main):
    def __init__(self, driver):
        self.driver=driver
        self.url="https://hrsa.cunyfirst.cuny.edu/psp/cnyhcprd/EMPLOYEE/HRMS/c/MANAGE_POSITIONS.POSITION_DATA.GBL"    
        self.searchfield="POSITION_SRCH_POSITION_NBR"
        self.nav()
    """    
    def nav(self):
        self.outer_instance.nav(self.url,self.searchfield)
    def move(self,num):
        self.outer_instance.move(num)
    """
        
    field1="POSITION_SRCH_POSITION_NBR"
    search="#ICSearch"
    add_row="$ICField3$new$0$$0"
    save="#ICSave"
    
    def return_switch(self):
        try:
            self.driver.switch_to.frame('TargetContent')
        except:
            self.driver.switch_to.default_content()
            
    def update_pos(self,corr=None,activate=None,dt=None,newrt=None,dept=None,title=None,line=None,payserv=None,reason=None):
        if corr:
            if self.windowswitch("#ICCorrection",0):    
                self.waitid("#ICCorrection")
                self.wait_spin()
        else:
            if self.windowswitch(self.add_row,0):
                self.waitid(self.add_row)
                self.wait_spin()
                sleep(1)
        if dept:
            if self.windowswitch('POSITION_DATA_DEPTID$0',0):
                print('udpating department')
                try:
                    self.waitfillid('POSITION_DATA_DEPTID$0',dept)
                except:
                    self.return_switch()
                    self.waitfillid('POSITION_DATA_DEPTID$0',dept)
                self.wait_spin()
                self.okay2()
                self.return_switch()
        if newrt:
            if self.windowswitch('POSITION_DATA_REPORTS_TO$0',0):
                print('udpating reports to')
                try:
                    self.waitfillid('POSITION_DATA_REPORTS_TO$0',newrt)
                except:
                    self.return_switch()
                    self.waitfillid('POSITION_DATA_REPORTS_TO$0',newrt)
                self.wait_spin()
                self.okay2()
                self.return_switch()
        if dt:
            if self.windowswitch('POSITION_DATA_EFFDT$0',0):
                print('udpating date')
                try:
                    self.waitfillid('POSITION_DATA_EFFDT$0',dt)
                except:
                    self.return_switch()
                    self.waitfillid('POSITION_DATA_EFFDT$0',dt)
                self.wait_spin()
                self.okay2()
                self.return_switch()
            else:
                print('udpating date')
                self.return_switch()
                self.waitfillid('POSITION_DATA_EFFDT$0',dt)
                self.wait_spin()
                self.okay2()
                self.return_switch()
        if reason:
            if self.windowswitch('POSITION_DATA_ACTION_REASON$0',0):
                print('udpating updating reason')
                try:
                    self.waitfillid('POSITION_DATA_ACTION_REASON$0',reason)
                except:
                    self.return_switch()
                    self.waitfillid('POSITION_DATA_ACTION_REASON$0',reason)
                self.wait_spin()
                self.okay2()
                self.return_switch()
        if activate:
            if self.windowswitch("POSITION_DATA_EFF_STATUS$0",0):
                if self.dropdownitembyid("POSITION_DATA_EFF_STATUS$0")!='Active':
                    print('udpating Effective Status')
                    try:
                        self.dropdownselector("POSITION_DATA_EFF_STATUS$0",'Active')
                    except:
                        self.return_switch()
                        self.dropdownselector("POSITION_DATA_EFF_STATUS$0",'Active')
                    self.wait_spin()
            if self.windowswitch("POSITION_DATA_POSN_STATUS$0",0):
                print('udpating position status')
                if self.dropdownitembyid("POSITION_DATA_POSN_STATUS$0")!='Approved':
                    try:
                        self.dropdownselector("POSITION_DATA_POSN_STATUS$0",'Approved')
                    except:
                        self.return_switch()
                        self.dropdownselector("POSITION_DATA_POSN_STATUS$0",'Approved')
                    self.wait_spin()
        if self.windowswitch("ICTAB_1",0):
            print('switching tabs')
            self.waitid("ICTAB_1")
            sleep(1)
        if self.windowswitch("POSITION_DATA_UPDATE_INCUMBENTS$0",0):
            print('udpating incumbent checkbox')
            try:
                self.waitid("POSITION_DATA_UPDATE_INCUMBENTS$0")
            except:
                self.return_switch()
                self.waitid("POSITION_DATA_UPDATE_INCUMBENTS$0")
            self.okay2()
        sleep(1)
        self.simplesave()
        self.okay2()
    def mass_rt_upd(self,poslist,effdt,posnum):
        successlist=[]
        faillist=[]
        for i in poslist:   #gotta gather position numbers from CF to create poslist
            self.nav()
            try:
                self.openrecord("pos",[i])
                self.update_pos(newrt=posnum,dt=effdt,reason='RTC')
                successlist.append(i)
            except:
                faillist.append(i)
                pass
        print('Successes:')
        print(','.join(successlist))
        print('Failures')
        print(','.join(faillist))
