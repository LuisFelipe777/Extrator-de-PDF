import olhoObaBranco from "../../assets/olho-oba-branco.svg"
import "./Header.css"
function Header(){
    return (
        <div className="header">
            <img src={olhoObaBranco} alt="" height={"100px"}/>
        </div>
    )

}
export default Header;
