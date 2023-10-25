public class PrimoTest
{
    public static void main(String[] args)
    {
        String mensagem = "CALCULANDO O MÁXIMO DIVISOR COMUM ENTRE";//Declara uma mensagem p/ início do App
        
        //Coloque os números desejados (LOGO ABAIXO)
        Primo PrimoTest1 = new Primo(54, 7);//Declara uma classe condutora juntamente com os valores

        System.out.printf("%s %d e %d %n", mensagem, PrimoTest1.getNum1(), PrimoTest1.getNum2());//Exibe uma mensagem
        int nn1 = PrimoTest1.maxNum();//Atribui o MAIOR número a nn1
        int nn2 = PrimoTest1.minNum();//Atribui o MENOR número a nn2
        int resto = -1;//inicia 'resto' como -1
       
        while ( resto != 0)
        {
            resto = nn1 % nn2;
            nn1 = nn2;
            if ( resto != 0)
            {
                nn2 = resto;
            }
        }
        System.out.printf("%nO máximo divisor comum é %d", nn2);

    }
}