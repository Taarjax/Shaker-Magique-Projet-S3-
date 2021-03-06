import React from "react";
import {
  apiDeleteNoteCocktail,
  apiGetCocktailUserNote,
  apiNoterCocktail,
  is_logged,
} from "../../Axios";
import ScoreBarButton from "./ScoreBarButton";
import "./ScoreBar.css";

export default function ScoreBar(props) {
  const [cocktailAvg, setCocktailAvg] = React.useState(props.cocktail.moyenne);
  const [userScore, setUserScore] = React.useState(0);

  // Récupérer la note de l'utilisateur
  React.useEffect(async () => {
    if (!props.readOnly && is_logged()) {
      setUserScore(await apiGetCocktailUserNote(props.cocktail.id));
    }
  }, []);

  /**
   * Retourne le niveau de remplissage,
   * selon la note et l'index du bouton
   * @param {*} index Index du bouton
   * @returns {string} full|half|empty
   */
  const getFilling = (index) => {
    const delta = cocktailAvg - (index - 1);

    if (delta >= 1) return "full";

    if (delta <= 0) return "empty";

    if (delta < 0.35) {
      return "empty";
    } else if (delta > 0.65) {
      return "full";
    } else {
      return "half";
    }
  };

  const getButtons = () => {
    const buttons = [];

    for (let i = 1; i <= 5; i++) {
      const active = !props.readOnly && i <= userScore;

      buttons.push(
        <ScoreBarButton
          key={i}
          index={i}
          filling={getFilling(i)}
          onClick={handleClick}
          size={props.size}
          active={active}
        />
      );
    }

    return buttons;
  };

  const handleClick = async (index) => {
    if (!props.readOnly && is_logged()) {
      let updatedAvg;

      // Si on a re-cliqué sur sa note, alors on retire la note
      if (index === userScore) {
        updatedAvg = await apiDeleteNoteCocktail(props.cocktail.id);
        index = 0;
      } else {
        updatedAvg = await apiNoterCocktail(props.cocktail.id, index);
      }

      setCocktailAvg(updatedAvg);
      setUserScore(index);
    }
  };

  return <div className="score-bar">{getButtons()}</div>;
}
