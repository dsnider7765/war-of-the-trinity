package com.wott.game.gui.screen;

import com.badlogic.gdx.*;
import com.badlogic.gdx.graphics.GL20;
import com.badlogic.gdx.graphics.OrthographicCamera;
import com.badlogic.gdx.graphics.g2d.Sprite;
import com.badlogic.gdx.graphics.g2d.SpriteBatch;
import com.badlogic.gdx.maps.MapObjects;
import com.badlogic.gdx.maps.objects.RectangleMapObject;
import com.badlogic.gdx.maps.tiled.TiledMap;
import com.badlogic.gdx.maps.tiled.TmxMapLoader;
import com.badlogic.gdx.maps.tiled.renderers.OrthogonalTiledMapRenderer;
import com.badlogic.gdx.math.Intersector;
import com.badlogic.gdx.math.MathUtils;
import com.badlogic.gdx.math.Rectangle;
import com.badlogic.gdx.math.Vector2;
import com.wott.game.WOTT;
import com.wott.game.game.encounter.Encounter;

/**
 * Created by student on 5/1/17.
 */
public class MainScreen implements Screen, InputProcessor{
    // Data Stuff
    private WOTT game;
    private Encounter[] mEncounters;

    // Render Stuff
    private SpriteBatch batch;
    private OrthographicCamera camera;
    private TiledMap map;
    private OrthogonalTiledMapRenderer mapRenderer;

    // Input Stuff
    private int keyCode;
    private int collisionLayer;
    private static final int nothingSelected = -5270;

    public MainScreen(WOTT game, String mapPath){
        this.game = game;

        batch = new SpriteBatch();
        camera = new OrthographicCamera();

        loadMap(Gdx.files.internal(mapPath).file().getAbsolutePath());
        collisionLayer = map.getLayers().getCount() - 1;

        mEncounters = new Encounter[5];
        for (int i = 0; i < 5; i++) {
            mEncounters[i] = new Encounter();
            boolean isSafe = false;
            Vector2 newPos = new Vector2();
            while (!isSafe) {
                int mapWidth = (int) (Math.round(Float.parseFloat(map.getProperties().get("tilewidth").toString())) * Float.parseFloat(map.getProperties().get("width").toString()));
                int mapHeight = (int) (Math.round(Float.parseFloat(map.getProperties().get("tileheight").toString())) * Float.parseFloat(map.getProperties().get("height").toString()));
                int xPos = MathUtils.random(50, mapWidth - 200);
                int yPos = MathUtils.random(50, mapHeight - 50);

                newPos = new Vector2(xPos, yPos);

                isSafe = !checkForCollision(newPos, mEncounters[i].getSprite().getBoundingRectangle());
            }
            mEncounters[i].getSprite().setPosition(newPos.x, newPos.y);
        }

        mapRenderer.setView(camera);
    }

    private boolean checkForCollision(Vector2 position, Rectangle hitbox){
        boolean hasCollided = false;

        MapObjects mapObjects = map.getLayers().get(collisionLayer).getObjects();
        for (RectangleMapObject mapObject: mapObjects.getByType(RectangleMapObject.class)) {
            hasCollided = Intersector.overlaps(hitbox, mapObject.getRectangle());
            if (hasCollided) break;
        }
        return hasCollided;
    }

    /**
     * Checks if the player's sprite is overlapping something.
     */
    private void checkForMovementCollision(Vector2 moveVector){
        System.out.println("Checking for Collision");
        boolean hasCollided = false;

        Rectangle playerHitBox = game.getPlayer().getSprite().getBoundingRectangle();
        Vector2 oldPos = playerHitBox.getPosition(new Vector2());
        Vector2 newPos = playerHitBox.getPosition(new Vector2()).add(moveVector);

        playerHitBox.setPosition(newPos);
        MapObjects mapObjects = map.getLayers().get(collisionLayer).getObjects();


        for (RectangleMapObject mapObject: mapObjects.getByType(RectangleMapObject.class)) {
            Rectangle hitBox = mapObject.getRectangle();
            hasCollided = Intersector.overlaps(playerHitBox, hitBox);
            if (hasCollided) break;
        }

        for (Encounter encounter: mEncounters) {
            Rectangle hitBox = encounter.getSprite().getBoundingRectangle();
            hasCollided = Intersector.overlaps(hitBox, playerHitBox);
            if (hasCollided) break;
        }

        int mapWidth = (int) (Math.round(Float.parseFloat(map.getProperties().get("tilewidth").toString())) * Float.parseFloat(map.getProperties().get("width").toString()));
        int mapHeight = (int) (Math.round(Float.parseFloat(map.getProperties().get("tileheight").toString())) * Float.parseFloat(map.getProperties().get("height").toString()));

        if (!hasCollided) {
            if (newPos.x < 0 || newPos.x + playerHitBox.getWidth() >= mapWidth) {
                hasCollided = true;
            }
            if (newPos.y < 0 || newPos.y + playerHitBox.getHeight() >= mapHeight) {
                hasCollided = true;
            }
        }

        if (hasCollided) {
            System.out.println("Collided!");
            camera.position.set(oldPos, 0);
        }
        else {
            camera.position.set(newPos, 0);
        }
    }

    private void loadMap(String path){
        TmxMapLoader loader = new TmxMapLoader();
        map = loader.load(path);
        mapRenderer = new OrthogonalTiledMapRenderer(map, batch);
        camera.setToOrtho(false, 19 * Float.parseFloat(map.getProperties().get("tilewidth").toString()),
                19 * Float.parseFloat(map.getProperties().get("tileheight").toString()));
        game.getPlayer().getSprite().setPosition(camera.position.x, camera.position.y);

        collisionLayer = map.getLayers().getCount() - 1;
    }

    private void fadeOut(){

    }

    @Override
    public void show() {

    }

    @Override
    public void render(float delta) {
        Gdx.gl.glClearColor(0, 0, 0, 1);
        Gdx.gl.glClear(GL20.GL_COLOR_BUFFER_BIT);

        Vector2 moveVector = new Vector2(0, 0);

        // Handle movement
//        switch (keyCode) {
//            case Input.Keys.LEFT:
//                moveVector.set(-300 * delta, 0);
//                break;
//            case Input.Keys.RIGHT:
//                moveVector.set(300 * delta, 0);
//                break;
//            case Input.Keys.UP:
//                moveVector.set(0, 300 * delta);
//                break;
//            case Input.Keys.DOWN:
//                moveVector.set(0, -300 * delta);
//                break;
//        }

        float speed = 300;
        if (Gdx.input.isKeyPressed(Input.Keys.SHIFT_LEFT) || Gdx.input.isKeyPressed(Input.Keys.SHIFT_RIGHT)) {
            speed = speed * 5;
        }

        if (Gdx.input.isKeyPressed(Input.Keys.LEFT)) {
            moveVector.add(-speed * delta, 0);
        }
        if (Gdx.input.isKeyPressed(Input.Keys.RIGHT)) {
            moveVector.add(speed * delta, 0);
        }
        if (Gdx.input.isKeyPressed(Input.Keys.UP)) {
            moveVector.add(0, speed * delta);
        }
        if (Gdx.input.isKeyPressed(Input.Keys.DOWN)) {
            moveVector.add(0, -speed * delta);
        }
        if (!moveVector.isZero()) {
            checkForMovementCollision(moveVector);
            camera.update();
        }

        game.getPlayer().getSprite().setPosition(camera.position.x, camera.position.y);

        mapRenderer.setView(camera);

        mapRenderer.render();
        batch.begin();
        for (Encounter encounter: mEncounters) {
            encounter.getSprite().draw(batch);
        }
        game.getPlayer().getSprite().draw(batch);
        batch.end();
    }

    @Override
    public void resize(int width, int height) {
        int tilesSide = Math.round(width / Float.parseFloat(map.getProperties().get("tilewidth").toString()));
        int tilesUpDown = Math.round(height / Float.parseFloat(map.getProperties().get("tileheight").toString()));

        float newWidth = tilesSide * Float.parseFloat(map.getProperties().get("tilewidth").toString());
        float newHeight = tilesUpDown * Float.parseFloat(map.getProperties().get("tileheight").toString());

        camera.setToOrtho(false, newWidth, newHeight);
        camera.position.set(newWidth / 2, newHeight / 2, 0);
    }

    @Override
    public void pause() {

    }

    @Override
    public void resume() {

    }

    @Override
    public void hide() {

    }

    @Override
    public void dispose() {
        map.dispose();
    }

    @Override
    public boolean keyDown(int keycode) {
        switch (keycode) {
            case Input.Keys.LEFT:
                keyCode = Input.Keys.LEFT;
                break;
            case Input.Keys.RIGHT:
                keyCode = Input.Keys.RIGHT;
                break;
            case Input.Keys.UP:
                keyCode = Input.Keys.UP;
                break;
            case Input.Keys.DOWN:
                keyCode = Input.Keys.DOWN;
                break;
            case Input.Keys.HOME:
                loadMap(Gdx.files.internal("maps/world-map/worldMap.tmx").file().getAbsolutePath());
                break;
        }
        return false;
    }

    @Override
    public boolean keyUp(int keycode) {
        if (keyCode == keycode) {
            keyCode = nothingSelected;
        }
        return false;
    }

    @Override
    public boolean keyTyped(char character) {
        return false;
    }

    @Override
    public boolean touchDown(int screenX, int screenY, int pointer, int button) {
        return false;
    }

    @Override
    public boolean touchUp(int screenX, int screenY, int pointer, int button) {
        return false;
    }

    @Override
    public boolean touchDragged(int screenX, int screenY, int pointer) {
        return false;
    }

    @Override
    public boolean mouseMoved(int screenX, int screenY) {
        return false;
    }

    @Override
    public boolean scrolled(int amount) {
        return false;
    }
}
