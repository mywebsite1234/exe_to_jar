import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.awt.image.BufferedImage;
import java.io.IOException;
import java.net.URL;
import java.util.ArrayList;
import java.util.Iterator;
import javax.imageio.ImageIO;
import javax.sound.sampled.*;

public class MarioGame extends JFrame {

    public MarioGame() {
        setTitle("Mario");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setResizable(false);
        
        GamePanel panel = new GamePanel();
        add(panel);
        pack();
        
        setLocationRelativeTo(null);
        setVisible(true);
        
        panel.startGame();
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(MarioGame::new);
    }
}

class GamePanel extends JPanel implements Runnable, KeyListener {

    final int width = 1000;
    final int height = 495;
    final int FPS = 60;
    
    int move = 0;
    int game = 1;
    int score = 0;
    int fire = 0;
    int no_fire = 0; 
    
    Thread gameThread;
    boolean keyLeft, keyRight, keyUp, keyLShift, keyLCtrl;

    // FIXED: Changed <Brick> to <Sprite> so it can hold Questions and Bricks
    ArrayList<Ground> ground_group = new ArrayList<>();
    ArrayList<Sprite> obstacle_group = new ArrayList<>(); 
    ArrayList<Goomba> goomba_group = new ArrayList<>();
    ArrayList<Fireball> fireball_group = new ArrayList<>();
    ArrayList<Coin> coin_group = new ArrayList<>();
    ArrayList<Mushroom> mushroom_group = new ArrayList<>();
    ArrayList<Flower> flower_group = new ArrayList<>();
    
    Mario mario;
    
    String[] map = {
        "b    h      h     h                                                                                                                                                    ",
        "b                                                                                                                                                                      ",
        "b                                                                                                                                                                      ",
        "b                                                                                                                                                                      ",
        "b                                                                                                                                                                      ",
        "b                                                                                                                                                                      ",
        "b                                                                             g  g                                                                                     ",
        "b          ...u..     .?.                                                    .........                                     s                                           ",
        "b  m                                                                                                                      ss                                           ",
        "b                    .                        ..  .                                                                      sss                                           ",
        "b                   ...                      ...  ..                      .f.                                           ssss                                           ",
        "b               ...   ..                    ....  ...                                                                  sssss           c                               ",
        "b    h                                     .....  ....         ?????                                                  ssssss                                           ",
        "b  t =      ==g    p      ==g     =       ......  .....                                                   gg         sssssss       l   #                               ",
        "b-----------------------------------------------  --------------------  -------------   -------------------------------------------------------------------------------",
        "b-----------------------------------------------  --------------------  -------------   -------------------------------------------------------------------------------",
        "b-----------------------------------------------  --------------------  -------------   -------------------------------------------------------------------------------"
    };

    Sound marioTheme = new Sound("mario_theme.wav");
    Sound jumpSound = new Sound("stomp.wav");
    Sound coinSound = new Sound("coin-sound.wav");
    Sound powerSound = new Sound("power-up.wav");
    Sound goombaBye = new Sound("goomba-destroy.wav");
    Sound ouchSound = new Sound("ouchs.wav"); 
    Sound gameOverSound = new Sound("game-over.wav");

    public GamePanel() {
        this.setPreferredSize(new Dimension(width, height));
        this.setBackground(new Color(116, 147, 246));
        this.setDoubleBuffered(true);
        this.addKeyListener(this);
        this.setFocusable(true);
        
        initGame();
    }

    public void initGame() {
        int size = 30;
        
        for (int r = 0; r < map.length; r++) {
            String row = map[r];
            for (int c = 0; c < row.length(); c++) {
                char tile = row.charAt(c);
                int x = c * size;
                int y = r * size;
                
                if (tile == 'b' || tile == '-') {
                     ground_group.add(new Ground(x, y, 0));
                }
                else if (tile == '.') {
                    ground_group.add(new Ground(x, y, 1));
                }
                else if (tile == '?') {
                    obstacle_group.add(new Question(x, y));
                }
                else if (tile == '=') {
                    obstacle_group.add(new Mquestion(x, y));
                }
                else if (tile == 'g') {
                    goomba_group.add(new Goomba(x, y));
                }
                else if (tile == 'm') {
                    mario = new Mario(x, y, this);
                }
                else if (tile == 'h') {
                     obstacle_group.add(new Brick(x, y));
                }
            }
        }
        
        if (mario == null) mario = new Mario(100, 300, this);
        marioTheme.loop();
    }

    public void startGame() {
        gameThread = new Thread(this);
        gameThread.start();
    }

    @Override
    public void run() {
        double drawInterval = 1000000000 / FPS;
        double delta = 0;
        long lastTime = System.nanoTime();
        long currentTime;
        
        while (gameThread != null) {
            currentTime = System.nanoTime();
            delta += (currentTime - lastTime) / drawInterval;
            lastTime = currentTime;
            
            if (delta >= 1) {
                update();
                repaint();
                delta--;
            }
        }
    }
    
    public void update() {
        if (game == 0) return;

        // FIXED: Added 'this' to the update call
        mario.update(this);
        
        if (mario.rect.x >= width / 2) {
            move = 1;
        }
        if (keyLeft && move == 1) {
            move = 0;
        }

        updateGroup(ground_group);
        updateGroup(obstacle_group);
        updateGroup(goomba_group);
        updateGroup(fireball_group);
        updateGroup(coin_group);
        updateGroup(mushroom_group);
        updateGroup(flower_group);
    }
    
    private void updateGroup(ArrayList<? extends Sprite> group) {
        Iterator<? extends Sprite> iter = group.iterator();
        while (iter.hasNext()) {
            Sprite s = iter.next();
            s.update(this);
            if (!s.alive) iter.remove();
        }
    }

    @Override
    public void paintComponent(Graphics g) {
        super.paintComponent(g);
        Graphics2D g2 = (Graphics2D) g;

        drawGroup(g2, ground_group);
        drawGroup(g2, obstacle_group);
        drawGroup(g2, goomba_group);
        drawGroup(g2, fireball_group);
        drawGroup(g2, coin_group);
        drawGroup(g2, mushroom_group);
        drawGroup(g2, flower_group);
        
        if (mario != null) mario.draw(g2);
        
        g2.setColor(Color.WHITE);
        g2.setFont(new Font("Arial", Font.BOLD, 20));
        g2.drawString("Score: " + score, 10, 25);
    }
    
    private void drawGroup(Graphics2D g2, ArrayList<? extends Sprite> group) {
        for (Sprite s : group) s.draw(g2);
    }

    @Override
    public void keyPressed(KeyEvent e) {
        int code = e.getKeyCode();
        if (code == KeyEvent.VK_LEFT) keyLeft = true;
        if (code == KeyEvent.VK_RIGHT) keyRight = true;
        if (code == KeyEvent.VK_UP) keyUp = true;
        if (code == KeyEvent.VK_SHIFT) keyLShift = true;
        if (code == KeyEvent.VK_CONTROL) keyLCtrl = true;
    }

    @Override
    public void keyReleased(KeyEvent e) {
        int code = e.getKeyCode();
        if (code == KeyEvent.VK_LEFT) keyLeft = false;
        if (code == KeyEvent.VK_RIGHT) keyRight = false;
        if (code == KeyEvent.VK_UP) keyUp = false;
        if (code == KeyEvent.VK_SHIFT) keyLShift = false;
        if (code == KeyEvent.VK_CONTROL) keyLCtrl = false;
    }

    @Override public void keyTyped(KeyEvent e) {}
}

class Sprite {
    public int x, y, width, height;
    public Rectangle rect;
    public BufferedImage image;
    public boolean alive = true;
    
    public Sprite(int x, int y, String filename) {
        this.x = x;
        this.y = y;
        try {
            URL url = getClass().getResource(filename);
            if (url != null) {
                image = ImageIO.read(url);
                this.width = image.getWidth();
                this.height = image.getHeight();
            } else {
                this.width = 30;
                this.height = 30;
            }
        } catch (IOException e) {
            this.width = 30;
            this.height = 30;
        }
        this.rect = new Rectangle(x, y, width, height);
    }
    
    public void draw(Graphics2D g2) {
        if (image != null) {
            g2.drawImage(image, x, y, width, height, null);
        } else {
            g2.setColor(Color.RED);
            g2.fillRect(x, y, width, height);
        }
    }
    
    public void update(GamePanel gp) {
        if (gp.move == 1) {
            if (gp.keyRight) {
                 this.x -= 10;
            }
        }
        this.rect.setLocation(x, y);
    }
}

class Mario extends Sprite {
    double velocityY = 0;
    boolean onGround = false;
    String direction = "right";
    
    public Mario(int x, int y, GamePanel gp) {
        super(x, y, "mario1.png");
    }
    
    @Override
    public void update(GamePanel gp) {
        velocityY += 1.5;
        y += velocityY;
        rect.y = y;
        
        onGround = false;
        checkVerticalCollision(gp.ground_group);
        checkVerticalCollision(gp.obstacle_group);
        
        if (gp.move == 0) {
            if (gp.keyRight) {
                x += 5;
                direction = "right";
            }
            if (gp.keyLeft) {
                x -= 5;
                direction = "left";
            }
        }
        
        if (gp.move == 1) {
             if (gp.keyRight) direction = "right";
             if (gp.keyLeft) direction = "left";
        }

        rect.x = x;
        checkHorizontalCollision(gp.obstacle_group);
        
        if ((onGround || y >= gp.height - 50) && gp.keyUp) {
            velocityY = -22;
            gp.jumpSound.play();
            onGround = false;
        }
        
        if (y > gp.height) {
            gp.game = 0;
            gp.gameOverSound.play();
            System.out.println("GAME OVER");
        }
    }
    
    private void checkVerticalCollision(ArrayList<? extends Sprite> walls) {
        for (Sprite wall : walls) {
            if (rect.intersects(wall.rect)) {
                if (velocityY > 0) {
                    y = wall.rect.y - height;
                    velocityY = 0;
                    onGround = true;
                } else if (velocityY < 0) {
                    y = wall.rect.y + wall.rect.height;
                    velocityY = 0;
                }
                rect.y = y;
            }
        }
    }

    private void checkHorizontalCollision(ArrayList<? extends Sprite> walls) {
         for (Sprite wall : walls) {
            if (rect.intersects(wall.rect)) {
                if (direction.equals("right")) {
                    x = wall.rect.x - width;
                } else {
                    x = wall.rect.x + wall.rect.width;
                }
                rect.x = x;
            }
        }
    }
}

class Ground extends Sprite {
    public Ground(int x, int y, int id) {
        super(x, y, "ground.png");
    }
}

class Brick extends Sprite {
    public Brick(int x, int y) {
        super(x, y, "mario-brick.png");
    }
}

class Question extends Sprite {
    boolean active = true;
    public Question(int x, int y) {
        super(x, y, "question.png");
    }
    
    @Override
    public void update(GamePanel gp) {
        super.update(gp);
        if (active && rect.intersects(gp.mario.rect)) {
            if (gp.mario.rect.y > y) { 
                active = false;
                gp.coin_group.add(new Coin(x, y - 30));
                gp.coinSound.play();
            }
        }
    }
}

class Mquestion extends Sprite {
    boolean active = true;
    public Mquestion(int x, int y) {
        super(x, y, "question.png");
    }
     @Override
    public void update(GamePanel gp) {
        super.update(gp);
        if (active && rect.intersects(gp.mario.rect)) {
             if (gp.mario.rect.y > y) {
                active = false;
                gp.mushroom_group.add(new Mushroom(x, y - 30));
                gp.powerSound.play();
             }
        }
    }
}

class Goomba extends Sprite {
    int speed = 2;
    public Goomba(int x, int y) {
        super(x, y, "goomba.png");
    }
    
    @Override
    public void update(GamePanel gp) {
        super.update(gp);
        x -= speed;
        rect.x = x;
        
        if (rect.intersects(gp.mario.rect)) {
            if (gp.mario.velocityY > 0 && gp.mario.rect.y < y) {
                this.alive = false;
                gp.goombaBye.play();
                gp.mario.velocityY = -10;
                gp.score += 100;
            } else {
                gp.ouchSound.play();
                gp.game = 0;
            }
        }
    }
}

class Coin extends Sprite {
    public Coin(int x, int y) {
        super(x, y, "coin2.png");
    }
}

class Mushroom extends Sprite {
    public Mushroom(int x, int y) {
        super(x, y, "mushroom.png");
    }
     @Override
    public void update(GamePanel gp) {
        super.update(gp);
        x += 2; 
        rect.x = x;
        if (rect.intersects(gp.mario.rect)) {
            this.alive = false;
            gp.fire = 1;
            gp.powerSound.play();
        }
    }
}

class Flower extends Sprite {
     public Flower(int x, int y) {
        super(x, y, "fire_flower.png");
    }
}

class Fireball extends Sprite {
    public Fireball(int x, int y) {
        super(x, y, "fireball.png");
    }
}

class Sound {
    Clip clip;
    public Sound(String filename) {
        try {
            URL url = getClass().getResource(filename);
            if (url != null) {
                AudioInputStream ais = AudioSystem.getAudioInputStream(url);
                clip = AudioSystem.getClip();
                clip.open(ais);
            }
        } catch (Exception e) {}
    }
    
    public void play() {
        if (clip != null) {
            clip.setFramePosition(0);
            clip.start();
        }
    }
    
    public void loop() {
        if (clip != null) {
            clip.loop(Clip.LOOP_CONTINUOUSLY);
        }
    }
}