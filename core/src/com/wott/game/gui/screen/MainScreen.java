package com.wott.game.gui.screen;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.Graphics;
import com.badlogic.gdx.Screen;
import com.badlogic.gdx.graphics.GL20;
import com.badlogic.gdx.graphics.OrthographicCamera;
import com.badlogic.gdx.graphics.g2d.SpriteBatch;
import com.badlogic.gdx.maps.MapLayer;
import com.badlogic.gdx.maps.MapObject;
import com.badlogic.gdx.maps.MapRenderer;
import com.badlogic.gdx.maps.tiled.TiledMap;
import com.badlogic.gdx.maps.tiled.TiledMapTileLayer;
import com.badlogic.gdx.maps.tiled.TmxMapLoader;
import com.badlogic.gdx.maps.tiled.renderers.BatchTiledMapRenderer;
import com.badlogic.gdx.maps.tiled.renderers.OrthogonalTiledMapRenderer;
import com.wott.game.WOTT;

import java.util.ArrayList;
import java.util.Iterator;

/**
 * Created by student on 5/1/17.
 */
public class MainScreen implements Screen{
    SpriteBatch batch;
    OrthographicCamera camera;
    WOTT game;
    TiledMap map;
    OrthogonalTiledMapRenderer mapRenderer;

    // DEBUG STUFF
    private float speedX = 1.0f;
    private float speedY = 1;

    public MainScreen(WOTT game){
        this.game = game;

        batch = new SpriteBatch();
        camera = new OrthographicCamera();
        loadMap("maps/talon/theMap.tmx");

        camera.setToOrtho(false, 19 * Float.parseFloat(map.getProperties().get("tilewidth").toString()),
                19 * Float.parseFloat(map.getProperties().get("tileheight").toString()));

        Iterator<String> keys = map.getProperties().getKeys();
        while(keys.hasNext()) {
            System.out.println(keys.next());
        }
        System.out.println(map.getProperties().get("height"));


        mapRenderer.setView(camera);

        System.out.println(Float.parseFloat(map.getProperties().get("height").toString()));
        System.out.println(speedX);
    }

    public void loadMap(String path){
        TmxMapLoader loader = new TmxMapLoader();
        map = loader.load(path);
        mapRenderer = new OrthogonalTiledMapRenderer(map, batch);
    }

    @Override
    public void show() {

    }

    @Override
    public void render(float delta) {
        Gdx.gl.glClearColor(0, 0, 0, 1);
        Gdx.gl.glClear(GL20.GL_COLOR_BUFFER_BIT);

        if (camera.position.x / mapRenderer.getUnitScale() >= Float.parseFloat(map.getProperties().get("width").toString())) {
            speedX = -speedX;
        }
        if (camera.position.y / mapRenderer.getUnitScale() >= Float.parseFloat(map.getProperties().get("height").toString())) {
            speedY = -speedY;
        }


        //camera.translate(speedX,0);
        camera.update();

        mapRenderer.setView(camera);

        mapRenderer.render();
        batch.begin();
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
}
