import java.util.TimerTask;

public class TimerTaskTest02 extends TimerTask {

        @Override
        public void run() {
            System.out.println("指定时间执行线程任务...");
        }
    }