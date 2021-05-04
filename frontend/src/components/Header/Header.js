import s from "./Header.module.css";
import logo from "../../static/logo.svg";
import { Link } from "react-router-dom";

function Header() {
  return (
    <header className={s.header}>
      {/* logo */}
      <span>
        <Link to="/">
          <img src={logo} alt="logo" />
        </Link>
      </span>

      {/* left subscription near logo */}
      <div>
        <Link to="/" className={s.header__subscription}>
          <span>GameStore</span>
        </Link>
      </div>

      {/* navbar */}
      <div className={s.header__nav}>
        <Link to="/" className={s.header__nav__link}>
          <span>Games</span>
        </Link>
        <Link to="/community" className={s.header__nav__link}>
          <span>Community</span>
        </Link>
        <Link to="/about" className={s.header__nav__link}>
          <span>About</span>
        </Link>
        <Link to="/support" className={s.header__nav__link}>
          <span>Support</span>
        </Link>
      </div>

      {/* user panel */}
      <div className={s.header__userbar}>
        <span>Sign in</span>
      </div>
    </header>
  );
}

export default Header;
