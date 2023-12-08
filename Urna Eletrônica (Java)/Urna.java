import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;
import java.util.HashMap;
import java.util.Map;

public class Urna
{
    public static void main(String[] args)
    {
        int candidato1 = 0;//NÚMERO DE VOTOS
        int candidato2 = 0;
        int candidato3 = 0;
        int anulados = 0;
        int firstVote = 0;

        Scanner ler = new Scanner(System.in);
        ArrayList<Integer> votos = new ArrayList<>();//LISTA DE VOTOS
        int x = 0;
        while (x == 0) {
            showMenu();
            int opcao = 0;
            while (true){//GARANTE QUE SEJA FORNECIDO UM INTEIRO
                try{
                    System.out.printf("%nEscolha uma opção: ");
                    opcao = ler.nextInt();
                    break;
                }
                catch (Exception e){
                    System.out.println("INSIRA UMA OPÇÃO VÁLIDA!");
                    ler.nextLine();
                }
            }
            
            switch (opcao)
            {//ANALIZA QUAL OPÇÃO FOI SELECIONADA
                case (0): {
                    System.out.printf("%nFINALIZANDO%n");
                    x = 1;
                    break;
                }
                case (1):{
                    votos.add(opcao);
                    candidato1++;
                    System.out.println("VOTO REGISTRADO COM SUCESSO!");
                    System.out.println();
                    break;
                }
                case (2):{
                    votos.add(opcao);
                    candidato2++;
                    System.out.println("VOTO REGISTRADO COM SUCESSO!");
                    System.out.println();
                    break;
                }
                case (3):{
                    votos.add(opcao);
                    candidato3++;
                    System.out.println("VOTO REGISTRADO COM SUCESSO!");
                    System.out.println();
                    break;
                }
                case (4):{
                    votos.add(opcao);
                    anulados++;
                    System.out.println("VOTO REGISTRADO COM SUCESSO!");
                    System.out.println();
                    break;
                }

                default:
                System.out.printf("%nPOR FAVOR. INSIRA UMA DAS OPÇÕES ACIMA");
                    break;       
            }//FIM DO SWITCH
        }//FIM DO WHILE

        int moda = calcularModa(votos);//ACHA QUEM FOI O VENCEDOR
        calulaPercent(candidato1, candidato2, candidato3, anulados, votos);//CALCULA O PERCENTUAL DE VOTOS
        showWinner(moda);
    }

    
    public static void showMenu()
    {  
        System.out.println("");
        System.out.println("================");
        System.out.println(" ELEIÇÕES 2024");
        System.out.println("================");
        System.out.println("1. CANDIDATO 1");
        System.out.println("2. CANDIDATO 2");
        System.out.println("3. CANDIDATO 3");
        System.out.println("4. ANULAR VOTO");
        System.out.println("0. FINALIZAR VOTAÇÃO");

    }
    public static int calcularModa(ArrayList<Integer> data) {
        // Contagem de ocorrências de cada valor
        Map<Integer, Integer> contagem = new HashMap<>();

        for (int valor : data) {
            contagem.put(valor, contagem.getOrDefault(valor, 0) + 1);
        }

        // Encontrar o valor com a contagem máxima
        int moda = 0;
        int maxContagem = 0;

        for (Map.Entry<Integer, Integer> entry : contagem.entrySet()) {
            if (entry.getValue() > maxContagem) {
                maxContagem = entry.getValue();
                moda = entry.getKey();
            }
        }
        return moda;
    }
    
    public static void showWinner(int m){
        //MOSTRA O VENCEDOR
        if (m == 1){
            System.out.printf("%nO Vencedor é o Candidato 1");
        }
        else if (m == 2){
            System.out.printf("%nO Vencedor é o Candidato 2");
        }
        else if (m == 3){
            System.out.printf("%nO Vencedor é o Candidato 3");
        }
        else if (m == 4){
            System.out.printf("%nAs Eleições foram canceladas");
        }

    }
    public static void calulaPercent(int c1, int c2, int c3, int a, ArrayList<Integer> osVotos )
    {//CALCULA O PERCENTUAL DE VOTOS
        if (osVotos.size() == 0){
            System.out.println("ELEIÇÃO CANCELADA! NENHUM VOTO REGISTRADO");
        }
        else{
            System.out.printf("%nCandidato 1 com %.2f%s dos Votos", ((double) c1/(double) osVotos.size())*100, "%");
            System.out.printf("%nCandidato 2 com %.2f%s dos Votos", ((double) c2/(double) osVotos.size())*100, "%");
            System.out.printf("%nCandidato 3 com %.2f%s dos Votos", ((double) c3/(double) osVotos.size())*100, "%");
            System.out.printf("%nVotos Anulados com %.2f%s dos Votos", ((double) a/(double) osVotos.size())*100, "%");
        }
        
    }
}