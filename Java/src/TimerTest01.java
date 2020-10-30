import java.util.Timer;

public class TimerTest01 {
        Timer timer;
        public TimerTest01(int time){
            timer = new Timer();
            timer.schedule(new TimerTaskTest01(), time * 1000);
        }

        public static void main(String[] args) {
            System.out.println("timer begin....");
            new TimerTest01(3);
        }
    }

