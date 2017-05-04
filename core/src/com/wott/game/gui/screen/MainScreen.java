package com.wott.game.gui.screen;

import com.badlogic.gdx.*;
import com.badlogic.gdx.graphics.GL20;
import com.badlogic.gdx.graphics.OrthographicCamera;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g2d.Sprite;
import com.badlogic.gdx.graphics.g2d.SpriteBatch;
import com.badlogic.gdx.graphics.g2d.TextureRegion;
import com.badlogic.gdx.maps.MapLayer;
import com.badlogic.gdx.maps.MapObject;
import com.badlogic.gdx.maps.MapObjects;
import com.badlogic.gdx.maps.MapRenderer;
import com.badlogic.gdx.maps.objects.RectangleMapObject;
import com.badlogic.gdx.maps.tiled.TiledMap;
import com.badlogic.gdx.maps.tiled.TiledMapTileLayer;
import com.badlogic.gdx.maps.tiled.TmxMapLoader;
import com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer;
import com.badlogic.gdx.maps.tiled.renderers.OrthogonalTiledMapRenderer;
import com.badlogic.gdx.math.Intersector;
import com.badlogic.gdx.math.Rectangle;
import com.badlogic.gdx.math.Vector2;
import com.wott.game.WOTT;

import java.util.ArrayList;
import java.util.Iterator;

/**
 * Created by student on 5/1/17.
 */
public class MainScreen implements Screen, InputProcessor{
    SpriteBatch batch;
    OrthographicCamera camera;
    WOTT game;
    TiledMap map;
    OrthogonalTiledMapRenderer mapRenderer;

    // Input stuff
    int keyCode;
    int collisionLayer = 4;

    // DEBUG STUFF
    private static final int nothingSelected = -5270;

    public MainScreen(WOTT game){
        this.game = game;

        batch = new SpriteBatch();
        camera = new OrthographicCamera();
        loadMap(Gdx.files.internal("maps/talon/theMap.tmx").file().getAbsolutePath());

        mapRenderer.setView(camera);
    }

    /**
     * Checks if the player's sprite is overlapping something.
     */
    private void checkForCollision(Vector2 moveVector){
        System.out.print("Starting collsion check...");
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

        if (hasCollided) {
            System.out.println("Collided!");
            camera.position.set(oldPos, 0);
        }
        else {
            System.out.println("Clear!");
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

        if (Gdx.input.isKeyPressed(Input.Keys.LEFT)) {
            moveVector.add(-300 * delta, 0);
        }
        if (Gdx.input.isKeyPressed(Input.Keys.RIGHT)) {
            moveVector.add(300 * delta, 0);
        }
        if (Gdx.input.isKeyPressed(Input.Keys.UP)) {
            moveVector.add(0, 300 * delta);
        }
        if (Gdx.input.isKeyPressed(Input.Keys.DOWN)) {
            moveVector.add(0, -300 * delta);
        }
        checkForCollision(moveVector);
        camera.update();

        game.getPlayer().getSprite().setPosition(camera.position.x, camera.position.y);

        mapRenderer.setView(camera);

        mapRenderer.render();
        batch.begin();
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
                loadMap(Gdx.files.internal("maps/talon/theMap.tmx").file().getAbsolutePath());
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
