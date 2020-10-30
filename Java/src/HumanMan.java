public class HumanMan extends HumanBeings implements WhatShouldHumanDo{
    @Override
    public void cook() {
        System.out.println("我是男人，我不需要做饭");
    }
    @Override
    public void work(){
        System.out.println("我是男人，我需要工作");
    }
}
