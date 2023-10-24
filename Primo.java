//CALCULA O MÁXIMO DIVISOR COMUM ENTRE DOIS NÚMEROS
//USANDO O ALGORITMO DE EUCLIDES

public class Primo
{
  private int num1;//Inicia as variáveis
  private int num2;//de Instância

  public Primo(int num1, int num2)//Construtor que recebe os dois números
  {
    this.num1 = num1;//Declara as variáveis
    this.num2 = num2;//^
  }
  public int getNum1()
  {
    return num1;
  }
  public int getNum2()
  {
    return num2;
  }
  public int maxNum()
  {
    return Math.max(num1, num2);//Retorna o maior número entre dois
  }
  public int minNum()
  {
    return Math.min(num1, num2);//Retorna o menor número entre dois
  }
}