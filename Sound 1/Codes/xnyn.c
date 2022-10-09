#include <stdio.h>

int main(){
    int i;
    int x[] = {1,2,3,4,2,1};
    float y[20];
    FILE*fp;
    y[0] = x[0];
    y[1] = x[1] - y[0]/2.0;
    for(i=2;i<20;i++){
        if(i<6)y[i] = x[i] + x[i-2] - y[i-1]/2.0;
        else y[i] = -y[i-1]/2.0;
    }
     fp = fopen("y.dat","w");
    for(i=0;i<20;i++){
        fprintf(fp,"%f\n",y[i]);
    }
    fclose(fp);
    
    return 0; 
}
