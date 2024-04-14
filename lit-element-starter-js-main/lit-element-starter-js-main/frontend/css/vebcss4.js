import {css} from 'lit';
export const vebcss4=css`
:host {
   display:block;
    max-width: 100%;
   

}

.mod {
    background-color: rgba(158, 158, 158, 0.75);
    max-width: 150px;
    width: 25%;
    text-align: center;
    border-radius: 15px;
    padding: 4px;
	
	
}
.mod1{
    position: relative;
   
    transform: rotatex(177deg);
}

.textB {
	display: inline-block;
    width: 28px;
    height: 28px;
    right: auto;
    top: auto;
    color: red;
    position: relative;
    border-radius: 50%;
    background-color: white;
    font-size: 1.2rem;
    text-align: center;
}


.textA { color: #795548;
    position: relative;
    border-radius: 5%;
    background-color: white;
    font-size: 0.8rem;
    text-align: center;
}

.table_grid {
   padding: 0 20px;
   
    grid-template-columns: repeat(4, 65px);
    justify-items: center;
    position: absolute;
    margin: 0 auto;
    bottom: 200px;
    left: 30%;
}
	

.table_grid span {
   
	background-color:#0098ff94;
	height:89px;
	width:57px;
	margin:5px;
	opacity: 0.2;
}


.mod:hover{ background-color:#2196F3;}


.super {
   margin: 0;
    height: 51vh;
    background-repeat: no-repeat;
    background-size: cover;
    display: flex;
    flex-direction: column;
	
}

.super_header{
	display: flex;
    align-items: center;
    justify-content: space-between;
    border-radius: 8px;
    padding: 8px;
    border: 4px solid rgb(0, 32, 113);
    background:#3F51B5; }

.super_header img{width: 20px;
    height: auto;
    position: relative;
    margin-left: -7px;}


h1, h2, h3, h4, h5, h6, p {
    padding: 0;
    margin: 0;
}

.data {
    background-color: white;
}



.text-h4 {
    text-align: center;
}

.header {
	min-height: 120px;
    display: flex;
    flex: 1 0 auto;
    position: relative;
    flex-direction: column;
    align-items: center;
	margin:0 auto;
	
}



.left {
   min-height: 120px;
    display: flex;
    flex: 1 0 auto;
    position: relative;
    flex-direction: column;
    align-items: center; 
   
}
.left {
   position:relative;
   width: auto;
  margin:0 auto;
}


.right {
  min-height: 120px;
    display: flex;
    flex: 1 0 auto;
    position: relative;
    flex-direction: column;
    align-items: center;  
  
}

.right {
   position:relative;
   width: auto;
  margin:0 auto;
}

.player-title {
   top: 3px;
    position: relative;
    
}

.player3CardsContainer {
    position: relative;
    max-width: 300px;
    height:auto;
    transform: scaleY(-1);
}

.player2CardsContainer {
    position: relative;
    max-width: 300px;
    height:auto;
    transform: scaleY(-1);
}

.player1CardsContainer {
    margin: 20px 0;
    position: relative;
    max-width: 300px;
    height: auto;
    transform: scaleY(-1);
	
	
}

.player0CardsContainer {
    margin: 20px 0;
    position: relative;
    width: 300px;
    height: 120px;
	margin-bottom: -20px;
}

.player1 {
    align-items: end;
}



.card_table {
}

.deck_card {
    position: absolute;
	width: 20%;
    height: auto;
}

.deck_flex {
   position: relative;
    width: 200px;
    display: flex;
    left: -73px;
    justify-content: center;
    align-items: center;
    top: 186px;
}







.footer {
  min-height: 150px;
    display: flex;
    justify-content: center;
    flex: 1 0 auto;
    top: 80%;
    position: relative;
    align-items: center;
}

.card_img {
    width: 57px;
    height: 89px;
    border-radius: 7px;
    transition: transform 250ms;
}

.cards_number-lastCard {
    transform: rotate(-90deg);
    position: absolute;
    right: 25%;
    z-index:auto;
}

.cards_number-6, .cards_number-5, .cards_number-4, .cards_number-3, .cards_number-2, .cards_number-1 {
    position: absolute;
}

.cards_number-6:nth-of-type(1) {
   
    
    left: 50px;
}

.cards_number-6:nth-of-type(2) {
   
   
    left: 80px;
}

.cards_number-6:nth-of-type(3) {
  
    left: 110px;
}

.cards_number-6:nth-of-type(4) {
  
    right: 110px;
}

.cards_number-6:nth-of-type(5) {
   
   
    right: 80px;
}

.cards_number-6:nth-of-type(6) {
  
   
    right: 50px;
}
.cards_number-6:nth-of-type(7) {
   
   
    right: 20px;
}

.cards_number-6:nth-of-type(8) {
   
   
    right: -10px;
}
.cards_number-6:nth-of-type(9) {
   
   
    right: -40px;
}

.cards_number-6:nth-of-type(10) {
   
    
    right:-70px;
}





.cards_number-6-hover:hover {
    box-shadow: 0px 0px 10px yellow;
	top:-20px;
}





.move-to-0 {
    transform: translateX(20px)
}
  
  .cards_number-55 {
	  position:relative;
   width: 57px;
    height: 89px;
    border-radius: 7px;  
}`