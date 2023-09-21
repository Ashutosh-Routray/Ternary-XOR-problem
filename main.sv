module ann;
  real x = -1;
  real y = -1;
  real in[1][0:2] = '{'{1,x,y}};
  real w1[0:2][0:4] = '{'{2.76542221,0.40939431,0.49996215,-0.17441179,1.67712425},'{-1.1320026,-3.90871511,-1.88363467,2.62882327,-0.13015998},'{-1.29875572,2.23490538,3.61552572,2.56542323,0.8478188}};
  real w2[0:5][1] = '{'{1.7450261},'{-1.44501008},'{-2.43414021},'{2.48834691},'{-2.26219307},'{-0.45983497}};
  real z1[1][0:4];
  real z2[1][0:5];
  real z3[1][1];
  real ans,an;
  
  always_comb
    begin
      z2[0][0]=1;
      for(int i=0;i<1;i++)
        begin
          for(int j=0;j<5;j++)
            begin
              ans=0;
              for(int k=0;k<3;k++)
                begin
                  ans+=in[i][k]*w1[k][j];
                end
              z1[i][j] = ans;
              z1[i][j]=$tanh(z1[i][j]);
              z2[0][j+1]=z1[0][j];
            end
        end
    end
  
    always_comb
    begin
      for(int i=0;i<1;i++)
        begin
          for(int j=0;j<1;j++)
            begin
              an=0;
              for(int k=0;k<6;k++)
                begin
                  an+=z2[i][k]*w2[k][j];
                end
              z3[i][j] = an;
              z3[i][j]=$tanh(z3[i][j]);
              if(z3[i][j]>0.5)z3[i][j]=1;
            else if(z3[i][j]<-0.5)z3[i][j]=-1;
            else z3[i][j]=0;
            end
        end
    end

  always_comb
    begin
    for(int i=0;i<1;i++)
      begin
        for(int j=0;j<1;j++)
          begin
            $display(z3[i][j]);
          end
      end
    end
endmodule
