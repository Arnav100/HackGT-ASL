import Button from "react-bootstrap/Button";
import { useNavigate } from "react-router-dom";

function CustomButton(props) {

  const navigate = useNavigate();
  const navigateToASL = () => {
    navigate('/asl')
  }
  return (
    <>
      <style type="text/css">
        {`
    .btn-flat {
      background-color: white;
      color: black;
      font-weight: bold;
    }
    .btn-flat:hover {
      background-color:#b31b1b;
      color: white;
    }
    .btn-xxl {
      padding: 1rem 1.5rem;
      font-size: 1.5rem;
    }
    `}
      </style>
      <Button variant="flat" size="xxl" onClick={navigateToASL}>{props.text}</Button>
    </>
  )
}

export default CustomButton