package com.wott.game.game.character.constants;

import java.util.HashMap;

/**
 * Created by student on 4/28/17.
 */
public class Element {
    public HashMap<ElementType, Double> advantages;

    public Element(ElementType ele){
        advantages = new HashMap<ElementType, Double>();
        switch(ele){
            case NON:
                break;
            case FIRE:
                advantages.put(ElementType.WATER, .45);
                advantages.put(ElementType.GRASS, 2.0);
                advantages.put(ElementType.ICE, 1.5);
                advantages.put(ElementType.POISON, 1.1);
                advantages.put(ElementType.GROUND, .3);
                advantages.put(ElementType.ROCK, .3);
                advantages.put(ElementType.METAL, 1.1);
                break;
            case WATER:
                advantages.put(ElementType.FIRE, 2.0);
                advantages.put(ElementType.GRASS, .5);
                advantages.put(ElementType.ICE, .9);
                advantages.put(ElementType.GROUND, .8);
                advantages.put(ElementType.ROCK, 1.2);
                advantages.put(ElementType.METAL, 1.2);
                break;
            case ELECTRIC:
                advantages.put(ElementType.WATER, 2.0);
                advantages.put(ElementType.ICE, 1.5);
                advantages.put(ElementType.GROUND, 0.0);
                advantages.put(ElementType.ROCK, 0.0);
                advantages.put(ElementType.METAL, .3);
                break;
            case GRASS:
                advantages.put(ElementType.FIRE, .5);
                advantages.put(ElementType.WATER, 2.0);
                advantages.put(ElementType.ELECTRIC, .8);
                advantages.put(ElementType.GRASS, .8);
                advantages.put(ElementType.ICE, 1.75);
                advantages.put(ElementType.POISON, .5);
                advantages.put(ElementType.GROUND, 1.2);
                advantages.put(ElementType.ROCK, 1.4);
                advantages.put(ElementType.METAL, .9);
                break;
            case ICE:
                advantages.put(ElementType.FIRE, 1.5);
                advantages.put(ElementType.WATER, 1.1);
                advantages.put(ElementType.ELECTRIC, .8);
                advantages.put(ElementType.GRASS, 1.3);
                advantages.put(ElementType.POISON, 1.2);
                advantages.put(ElementType.ROCK, 1.2);
                advantages.put(ElementType.METAL, 1.2);
                break;
            case POISON:
                advantages.put(ElementType.NON, 2.0);
                advantages.put(ElementType.WATER, .5);
                advantages.put(ElementType.GRASS, 1.5);
                advantages.put(ElementType.ICE, .8);
                advantages.put(ElementType.GROUND, .0);
                advantages.put(ElementType.ROCK, .0);
                advantages.put(ElementType.METAL, .0);
                break;
            case GROUND:
                advantages.put(ElementType.FIRE, 1.9);
                advantages.put(ElementType.WATER, 1.2);
                advantages.put(ElementType.ELECTRIC, 2.0);
                advantages.put(ElementType.GRASS, .8);
                advantages.put(ElementType.POISON, 2.0);
                advantages.put(ElementType.ROCK, .8);
                advantages.put(ElementType.METAL, .2);
                break;
            case ROCK:
                advantages.put(ElementType.FIRE, 1.7);
                advantages.put(ElementType.WATER, .7);
                advantages.put(ElementType.ELECTRIC, 2.0);
                advantages.put(ElementType.GRASS, .7);
                advantages.put(ElementType.POISON, 2.0);
                advantages.put(ElementType.GROUND, 1.2);
                advantages.put(ElementType.METAL, .2);
                break;
            case DARK:
                for (ElementType elementType: ElementType.values()) {
                    advantages.put(elementType, 1.5);
                }
                advantages.put(ElementType.LIGHT, 0.0);
                break;
            case LIGHT:
                advantages.put(ElementType.DARK, 4.0);
                break;
            case METAL:
                advantages.put(ElementType.ELECTRIC, 1.7);
                advantages.put(ElementType.POISON, 1.5);
                advantages.put(ElementType.GROUND, 1.5);
                advantages.put(ElementType.ROCK, 1.5);
                break;
        }
    }

    public Double getAdvantage(ElementType ele) {
        if (getAdvantages().containsKey(ele)) {
            return getAdvantages().get(ele);
        }
        return 1.0;
    }

    public HashMap<ElementType, Double> getAdvantages() {
        return advantages;
    }

    public void setAdvantages(HashMap<ElementType, Double> advantages) {
        this.advantages = advantages;
    }
}
