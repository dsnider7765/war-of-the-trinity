package com.wott.game.game.character.constants;

import java.util.HashMap;

/**
 * Created by student on 4/28/17.
 */
public class Body {
    public HashMap<BodyType, Double> advantages;

    public Body(BodyType ele){
        advantages = new HashMap<BodyType, Double>();
        switch(ele) {
            case BEAST:
                advantages.put(BodyType.HULKING, .8);
                advantages.put(BodyType.AMORPHOUS, .6);
                advantages.put(BodyType.STRETCHED, 1.2);
                advantages.put(BodyType.ABERRANT, .5);
                advantages.put(BodyType.CYBORG, .6);
                advantages.put(BodyType.CYBEAST, .8);
                advantages.put(BodyType.ELEMENTAL, .9);
                advantages.put(BodyType.LYCANTHROPE, .8);
                break;
            case HUMANOID:
                advantages.put(BodyType.HULKING, .8);
                advantages.put(BodyType.AMORPHOUS, .7);
                advantages.put(BodyType.STRETCHED, 1.1);
                advantages.put(BodyType.ABERRANT, .6);
                advantages.put(BodyType.CYBORG, .7);
                advantages.put(BodyType.CYBEAST, .9);
                advantages.put(BodyType.ELEMENTAL, .9);
                advantages.put(BodyType.LYCANTHROPE, .9);
                break;
            case HULKING:
                advantages.put(BodyType.BEAST, 1.5);
                advantages.put(BodyType.HUMANOID, 1.5);
                advantages.put(BodyType.AMORPHOUS, .5);
                advantages.put(BodyType.STRETCHED, 1.8);
                advantages.put(BodyType.ABERRANT, .4);
                advantages.put(BodyType.CYBEAST, 1.2);
                advantages.put(BodyType.ELEMENTAL, .5);
                advantages.put(BodyType.LYCANTHROPE, 1.2);
                advantages.put(BodyType.STRANGE, 1.3);
                break;
            case AMORPHOUS:
                advantages.put(BodyType.AMORPHOUS, 1.4);
                advantages.put(BodyType.HUMANOID, 1.2);
                advantages.put(BodyType.HULKING, 1.7);
                advantages.put(BodyType.CYBEAST, 1.2);
                advantages.put(BodyType.STRANGE, 1.3);
                break;
            case STRETCHED:
                advantages.put(BodyType.BEAST, .9);
                advantages.put(BodyType.HULKING, .5);
                advantages.put(BodyType.AMORPHOUS, .9);
                advantages.put(BodyType.ABERRANT, .9);
                advantages.put(BodyType.CYBORG, .6);
                advantages.put(BodyType.CYBEAST, .8);
                advantages.put(BodyType.ELEMENTAL, .8);
                advantages.put(BodyType.STRANGE, 1.1);
                break;
            case ABERRANT:
                for (BodyType bodyType: BodyType.values()) {
                    advantages.put(bodyType, 1.1);
                }
                advantages.put(BodyType.ABERRANT, 2.0);
                advantages.put(BodyType.CYBEAST, 1.3);
                advantages.put(BodyType.ELEMENTAL, 1.5);
                advantages.put(BodyType.STRANGE, .9);
                break;
            case CYBORG:
                advantages.put(BodyType.BEAST, 1.2);
                advantages.put(BodyType.HUMANOID, 1.1);
                advantages.put(BodyType.STRETCHED, 1.5);
                advantages.put(BodyType.ABERRANT, 0.7);
                advantages.put(BodyType.CYBEAST, 1.4);
                advantages.put(BodyType.LYCANTHROPE, 1.1);
                advantages.put(BodyType.STRANGE, 0.9);
                break;
            case CYBEAST:
                advantages.put(BodyType.BEAST, 1.2);
                advantages.put(BodyType.HUMANOID, 1.1);
                advantages.put(BodyType.HULKING, .8);
                advantages.put(BodyType.AMORPHOUS, .8);
                advantages.put(BodyType.STRETCHED, 1.2);
                advantages.put(BodyType.ABERRANT, .7);
                advantages.put(BodyType.CYBORG, .6);
                advantages.put(BodyType.ELEMENTAL, .9);
                advantages.put(BodyType.LYCANTHROPE, .8);
                advantages.put(BodyType.STRANGE, .8);
                break;
            case ELEMENTAL:
                advantages.put(BodyType.BEAST, 1.2);
                advantages.put(BodyType.HUMANOID, 1.1);
                advantages.put(BodyType.HULKING, 1.5);
                advantages.put(BodyType.STRETCHED, 1.2);
                advantages.put(BodyType.ABERRANT, 0.5);
                advantages.put(BodyType.CYBEAST, 1.1);
                advantages.put(BodyType.LYCANTHROPE, 1.4);
                break;
            case LYCANTHROPE:
                advantages.put(BodyType.BEAST, 1.2);
                advantages.put(BodyType.HUMANOID, 1.1);
                advantages.put(BodyType.HULKING, .8);
                advantages.put(BodyType.ABERRANT, .9);
                advantages.put(BodyType.CYBORG, .9);
                advantages.put(BodyType.CYBEAST, 1.2);
                advantages.put(BodyType.ELEMENTAL, .6);
                advantages.put(BodyType.STRANGE, .9);
                break;
            case STRANGE:
                advantages.put(BodyType.HULKING, .7);
                advantages.put(BodyType.AMORPHOUS, .7);
                advantages.put(BodyType.STRETCHED, .9);
                advantages.put(BodyType.ABERRANT, 1.1);
                advantages.put(BodyType.CYBORG, 1.1);
                advantages.put(BodyType.CYBEAST, 1.2);
                advantages.put(BodyType.LYCANTHROPE, 1.1);
                break;
        }
    }

    public Double getAdvantage(BodyType ele) {
        if (getAdvantages().containsKey(ele)) {
            return getAdvantages().get(ele);
        }
        return 1.0;
    }

    public HashMap<BodyType, Double> getAdvantages() {
        return advantages;
    }

    public void setAdvantages(HashMap<BodyType, Double> advantages) {
        this.advantages = advantages;
    }
}
