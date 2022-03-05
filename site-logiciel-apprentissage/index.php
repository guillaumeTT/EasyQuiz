<!DOCTYPE html>
<html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Projet Personnel</title>
        <link rel="stylesheet" type="text/css" href="index.css">
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Fredoka">

        <script src="https://code.jquery.com/jquery-latest.js"></script>
        <script src="https://code.jquery.com/ui/1.10.3/jquery-ui.js"></script>
    </head>
    <body>
        <h1>Le logiciel d'apprentissage </h1>

        <nav id="fil_ariane">
            <ul>
                <li><a href="#objectif">L'objectif de ce logiciel</a></li>
                <li><a href="#presentation">Présentation de l'interface</a></li>
                <li><a href="#selection">Sélection d'un élément dans liste</a></li>
                <li><a href="#apprentissage">Phase d'apprentissage</a></li>
            </ul>
        </nav>
        <section>
            <h2 id="objectif">L'objectif de ce logiciel</h2>
            <p>Apprendre des choses, c'est bien. Mais les retenir sur le long terme, c'est mieux.<br>
                C'est pour cela que j'ai créé ce logiciel pour pouvoir m'aider à mieux apprendre. <br>
                Le projet en tant que tel est fini. Mais nous pouvons toujours rajouter <br>
                des fonctionnalités pour plus de cohérence dans son utilisation.
            </p>
        </section>
        <section>
            <div class="image-group">
            <div class="row">
                <img class="image" id="img1" src="img/img1.png" alt="Représentation de l'interface dans sa globalité">
                <p>image 1</p>
            </div>
            <div class="row">
            <h2 id="presentation">Présentation de l'interface</h2>  
            <p>Voici à quoi ressemble l'interface, un fois avoir lancé tkinterQuiz.py.<br>
            Sur la gauche, c'est ici que nous verrons les éléments que nous devrons deviner.<br>
            Et la barre de couleur qui va du rouge au vert, c'est ici que l'on verra <br>
            le nombre de mots ou autres dans chacune des cases.
            </p>
            <p>
            Sur la droite, on pourra sélectionner ce qu'on veut apprendre pour s'améliorer. <br>
            Pour voir les autres éléments qu'on a ajouté mais que nous voyons pas dans la liste, <br>
            nous pouvons scroller dans la liste pour voir les éléments en dessous.
            </p>
            <p>
            Pour le menu, tout n'est pas encore fonctionnel. Cependant, dans "Sélection",<br>
            nous pouvons lister l'ensemble des boîtes avec le contenu des boîtes.
            </p>
            </div>
        </section>
        <section>
            <div class="bottom">
                <h2 id="selection">Sélection d'un élément dans liste</h2>
                <p>Pour sélectionner ce que l'on veut apprendre, on choisit dans la liste <br/>
                quelque chose qui nous intéresse. (image 2) <br/> <br/>
                Puis, nous cliquons sur "J'ai fais mon choix" pour commencer l'apprentissage. (image 3)
                </p>
            </div>
            <div class="image-group">
                <div class="row">
                    <img class="image" id="img2" src="img/img2.png" alt="Sélection de l'élément dans la liste">
                    <p>image 2</p>
                </div>
                <div class="row">
                    <img class="image" id="img3" src="img/img3.png" alt="Validation de l'élément">
                    <p>image 3</p>
                </div>
            </div>
        </section>
        <section>
            <div class="bottom">
                <h2 id="apprentissage">Phase d'apprentissage</h2>
                <p>Commençons à apprendre. Quand tu as fais ton choix, un élément apparait sur la gauche. <br>
                C'est à cette endroit que les éléments à savoir apparaitront. (image 4)
                </p>
                <p>
                Si tu connais on non la réponse de l'élément à savoir, alors, tu peux cliquer sur "oui" ou "non". <br>
                Mais si tu veux afficher la réponse, tu peux le faire en cliquant sur "Afficher la réponse". (image 5)</p>
                <p>
                Si tu as deviné la réponse, un autre élément à savoir va apparaître et le numéro changera <br>
                dans la case orange. Si tu ne savais pas la réponse et que tu cliques sur "Non", alors le <br>
                numéro changera dans la case rouge. Plus tu connaîtras un élément, plus il ira vers le vert. (image 6)
                </p>
            </div>
            <div class="image-group">
                <div class="row">
                    <img class="image" id="img4" src="img/img4.png" alt="Apparition de l'élément à apprendre">
                    <p>image 4</p>
                </div>
                <div class="row">
                    <img class="image" id="img5" src="img/img5.png" alt="Action du bouton pour afficher la réponse">
                    <p>image 5</p>
                </div>
                <div class="row">
                    <img class="image" id="img6" src="img/img6.png" alt="Action du bouton si oui ou non tu as deviner la réponse">
                    <p>image 6</p>
                </div>
            </div>
        </section>
        <footer>
            <p>Site réalisé en HTML/CSS, Javascript et JQuery</p>
        </footer>
        
        
        <script>
        
        function get_top_element(element){
            return $(element).offset().top; 
        }
        function get_bottom_element(element){
            return $(element).offset().top + $(element).outerHeight(); 
        }

        $(function() {
            $('.image').hide();

            function detect_visibility(){
                var bottom_of_screen = $(window).scrollTop() + $(window).innerHeight();
                var top_of_screen = $(window).scrollTop();

                if ((bottom_of_screen > get_top_element("#presentation")) && 
                (top_of_screen < get_bottom_element("#presentation"))){
                    $("#img1").fadeIn(2000);
                }
                if ((bottom_of_screen > get_top_element("#selection")) && 
                (top_of_screen < get_bottom_element("#selection"))){
                    $("#img2").fadeIn(2000);
                    $("#img3").fadeIn(2000);
                }
                if ((bottom_of_screen > get_top_element("#apprentissage")) && 
                (top_of_screen < get_bottom_element("#apprentissage"))){
                    $("#img4").fadeIn(2000);
                    $("#img5").fadeIn(2000);
                    $("#img6").fadeIn(2000);
                }
            }

        $(window).scroll(function() {
            detect_visibility();
        });

        detect_visibility();
        })       

        </script>

    </body>
</html>