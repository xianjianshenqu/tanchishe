import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import javax.sound.sampled.*;

public class Main {
    private static int speed = 150; // 默认速度
    private static int width = 800; // 默认宽度
    private static int height = 600; // 默认高度
    private static Clip eatSound;
    private static Clip gameOverSound;

    public static void main(String[] args) {
        // 加载声音
        loadSounds();
        
        // 创建主窗口
        JFrame frame = new JFrame("贪吃蛇游戏");
        
        // 创建菜单栏
        JMenuBar menuBar = new JMenuBar();
        
        // 设置菜单
        JMenu settingsMenu = new JMenu("设置");
        
        // 难度设置子菜单
        JMenu difficultyMenu = new JMenu("难度");
        ButtonGroup difficultyGroup = new ButtonGroup();
        JRadioButtonMenuItem easy = new JRadioButtonMenuItem("简单");
        JRadioButtonMenuItem medium = new JRadioButtonMenuItem("中等", true);
        JRadioButtonMenuItem hard = new JRadioButtonMenuItem("困难");
        difficultyGroup.add(easy);
        difficultyGroup.add(medium);
        difficultyGroup.add(hard);
        difficultyMenu.add(easy);
        difficultyMenu.add(medium);
        difficultyMenu.add(hard);
        
        // 速度设置子菜单
        JMenu speedMenu = new JMenu("速度");
        ButtonGroup speedGroup = new ButtonGroup();
        JRadioButtonMenuItem slow = new JRadioButtonMenuItem("慢速");
        JRadioButtonMenuItem normal = new JRadioButtonMenuItem("正常", true);
        JRadioButtonMenuItem fast = new JRadioButtonMenuItem("快速");
        speedGroup.add(slow);
        speedGroup.add(normal);
        speedGroup.add(fast);
        speedMenu.add(slow);
        speedMenu.add(normal);
        speedMenu.add(fast);
        
        // 窗口大小设置子菜单
        JMenu sizeMenu = new JMenu("窗口大小");
        ButtonGroup sizeGroup = new ButtonGroup();
        JRadioButtonMenuItem small = new JRadioButtonMenuItem("小 (600x400)");
        JRadioButtonMenuItem mediumSize = new JRadioButtonMenuItem("中 (800x600)", true);
        JRadioButtonMenuItem large = new JRadioButtonMenuItem("大 (1024x768)");
        sizeGroup.add(small);
        sizeGroup.add(mediumSize);
        sizeGroup.add(large);
        sizeMenu.add(small);
        sizeMenu.add(mediumSize);
        sizeMenu.add(large);
        
        // 添加菜单项
        settingsMenu.add(difficultyMenu);
        settingsMenu.add(speedMenu);
        settingsMenu.add(sizeMenu);
        menuBar.add(settingsMenu);
        
        // 声音设置
        JCheckBoxMenuItem soundItem = new JCheckBoxMenuItem("开启声音", true);
        menuBar.add(soundItem);
        
        frame.setJMenuBar(menuBar);
        
        // 创建游戏面板
        GamePanel gamePanel = new GamePanel(speed, width, height);
        frame.add(gamePanel);
        
        // 设置窗口属性
        frame.setSize(width, height);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLocationRelativeTo(null);
        frame.setVisible(true);
        
        // 添加菜单事件监听器
        addMenuListeners(easy, medium, hard, slow, normal, fast, small, mediumSize, large, soundItem, gamePanel, frame);
    }
    
    private static void loadSounds() {
        try {
            // 这里需要替换为你的声音文件路径
            AudioInputStream eatAudio = AudioSystem.getAudioInputStream(
                Main.class.getResourceAsStream("/sounds/eat.wav"));
            eatSound = AudioSystem.getClip();
            eatSound.open(eatAudio);
            
            AudioInputStream gameOverAudio = AudioSystem.getAudioInputStream(
                Main.class.getResourceAsStream("/sounds/gameover.wav"));
            gameOverSound = AudioSystem.getClip();
            gameOverSound.open(gameOverAudio);
        } catch (Exception e) {
            System.err.println("加载声音文件失败: " + e.getMessage());
        }
    }
    
    private static void addMenuListeners(JRadioButtonMenuItem easy, JRadioButtonMenuItem medium, JRadioButtonMenuItem hard,
                                       JRadioButtonMenuItem slow, JRadioButtonMenuItem normal, JRadioButtonMenuItem fast,
                                       JRadioButtonMenuItem small, JRadioButtonMenuItem mediumSize, JRadioButtonMenuItem large,
                                       JCheckBoxMenuItem soundItem, GamePanel gamePanel, JFrame frame) {
        // 难度设置监听
        easy.addActionListener(e -> gamePanel.setDifficulty(1));
        medium.addActionListener(e -> gamePanel.setDifficulty(2));
        hard.addActionListener(e -> gamePanel.setDifficulty(3));
        
        // 速度设置监听
        slow.addActionListener(e -> {
            speed = 200;
            gamePanel.setSpeed(speed);
        });
        normal.addActionListener(e -> {
            speed = 150;
            gamePanel.setSpeed(speed);
        });
        fast.addActionListener(e -> {
            speed = 100;
            gamePanel.setSpeed(speed);
        });
        
        // 窗口大小设置监听
        small.addActionListener(e -> {
            width = 600;
            height = 400;
            frame.setSize(width, height);
            gamePanel.setSize(width, height);
        });
        mediumSize.addActionListener(e -> {
            width = 800;
            height = 600;
            frame.setSize(width, height);
            gamePanel.setSize(width, height);
        });
        large.addActionListener(e -> {
            width = 1024;
            height = 768;
            frame.setSize(width, height);
            gamePanel.setSize(width, height);
        });
        
        // 声音设置监听
        soundItem.addActionListener(e -> {
            gamePanel.setSoundEnabled(soundItem.isSelected());
        });
    }
}