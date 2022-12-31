#include "TH1.h"
#include "TCanvas.h"
void hist_two(){
	TRandom2 *rand = new TRandom2(0);
	TH1F *hist = new TH1F("Pasos Posibles","Pasos posibles",3,0,2.5);
	double a = 0;
	int steps = 100000;
	for(int j =0; j < steps; j++){
		double r = rand->Rndm();
		if(r <= 0.5){
			a = 0;
		}else{
			a = 1;
		}
		hist->Fill(a);
	}
	hist->Scale(1/hist->GetEntries());
	hist->SetTitle(";;N/n");
	hist->GetXaxis()->SetBinLabel(1,"n1");
	hist->GetXaxis()->SetBinLabel(2,"n2");
	TCanvas *c1 = new TCanvas();
	c1->SetGrid();
	hist->SetBarWidth(0.5);
	hist->SetBarOffset(0.2);
	hist->SetFillColor(2);
	hist->Draw("bar");
}
