package com.wott.game.gui.screen;

import com.badlogic.gdx.Gdx;
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
        camera.setToOrtho(false, 3200, 3200);

        TmxMapLoader loader = new TmxMapLoader();
        System.out.println(Gdx.files.absolute("theMap.tmx"));
        map = loader.load("maps/python/theMap.tmx");

        System.out.println(map.getProperties().get("width"));
        Iterator<String> keys = map.getProperties().getKeys();
        while(keys.hasNext()) {
            System.out.println(keys.next());
        }
        System.out.println(map.getProperties().get("height"));

        mapRenderer = new OrthogonalTiledMapRenderer(map, batch);
        mapRenderer.setView(camera);

        System.out.println(Float.parseFloat(map.getProperties().get("height").toString()));
        System.out.println(speedX);
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


        camera.translate(speedX,0);
        camera.update();

        mapRenderer.setView(camera);

        mapRenderer.render();
        batch.begin();
        batch.end();
    }

    @Override
    public void resize(int width, int height) {

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
